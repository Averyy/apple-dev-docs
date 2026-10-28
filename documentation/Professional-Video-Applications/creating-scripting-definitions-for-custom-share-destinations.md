# Creating Scripting Definitions for Custom Share Destinations

**Framework**: Professional-Video-Applications  
**Role**: Article

Define the record types, object classes, and event types that let your app interact with Final Cut Pro.

## Overview

As the target application of a Final Cut Pro custom share destination, your app must respond to the Apple events that Final Cut Pro sends to get information about the kind of data your users want. (See [Responding to Apple Events from Final Cut Pro](./responding-to-apple-events-from-final-cut-pro.md).) Your app must also supply *scripting definitions* to define the Apple events along with their associated objects and record types. The tables in the following sections describe the definitions your app needs for its interactions with Final Cut Pro.

> **Note**:  For an example of a complete scripting definition, see [Review a Scripting Definition Example: Asset Management Suite](./creating-scripting-definitions-for-custom-share-destinations.md#Review-a-Scripting-Definition-Example-Asset-Management-Suite).

### Define Record Types

`asset location—`Describes the location of the files associated with an object of a class asset. (See [Define Object Classes](./creating-scripting-definitions-for-custom-share-destinations.md#Define-Object-Classes).)

| Property | Type | Description |
| --- | --- | --- |
| `folder` | `file` | The containing folder path. |
| `base name` | `text` | The base name for the exported output files. This name must match the asset name. |
| `has description` | `boolean` | Set to `true` if the app requires FCPXML as the exported output. |
| `has media` | `boolean` | Set to `true` if the app requires media as the exported output. |

`library location—`Describes the location of the library files associated with an asset.

| Property | Type | Description |
| --- | --- | --- |
| `library folder` | `file` | The containing folder path. |
| `library base name` | `text` | The base name for the exported output files. |
| `has archive` | `boolean` | Set to `true` if the application requires a library archive as the exported output. |
| `has library description` | `boolean` | Set to `true` if the application requires FCPXML as the exported output. |

### Define Object Classes

`asset—`Represents an asset object that corresponds to the exported output from Final Cut Pro.

| Property | Type | Description |
| --- | --- | --- |
| `id` | `text` | The unique asset identifier. |
| `name` | `text` | The asset name. |
| `location info` | `asset location` | The location of files associated with the asset. |
| `library info` | `library location` | The location of the library files associated with the asset. |
| `metadata` | `user defined record` | The shared metadata set associated with the asset. |
| `data options` | `user defined record` | The options set for the asset data. |

The protocol between Final Cut Pro and your app through Apple events should be agnostic to your app’s object containment hierarchy. For example, the scripting definition in the Asset Management Suite Example defines an asset as a document element, but it could also define an asset as an element of a larger entity, such as a media asset database.

Your app needs only to return an object specifier with which Final Cut Pro can access a specific asset object. (See [Review a Scripting Definition Example: Asset Management Suite](./creating-scripting-definitions-for-custom-share-destinations.md#Review-a-Scripting-Definition-Example-Asset-Management-Suite).)

When an asset object is not a document, handling an `Open` `Document` Apple event to associate files to an asset might be a bit awkward. Because Cocoa Scripting handles the `Open` `Document` Apple event, you need a custom document controller to override the behavior of Cocoa when your app opens a file and when it associates a file (based on matching the URL) with either an existing asset object or with a new asset object. You may need some customization to ensure that the files handled through the `Open` `Document` Apple event are properly associated to the asset object.

### Define Event Types

`make—`Creates a new asset object.

| Property | Type | Description |
| --- | --- | --- |
| `new` | `type` | The new object’s class. |
| `at` | `location specifier` | The location in which to insert the new object.* |
| `with data` | `any` | The initial contents of the object.* |
| `with` `properties` | `record` | A list of object properties used to initialize the new object: ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `name` (`text`)—The asset name. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `metadata` (`record`)—The metadata set associated with the asset object. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `data` `options` (`record`)—The option set used to create the asset data. |

> **Note**: Final Cut Pro doesn’t use the `at` and `with data` parameters itself, but they are inherited from the respective event definitions (or `make` event definitions) in the standard suite. They’re included here in case your app needs to support these parameters for other clients.

### Specify an Access Group for Your App

To enable access from a sandboxed application to the objects and events in your app, your app must specify `com.apple.assetmanagement.import` as the access group for:

- The object class for media assets
- The respective element in its container
- The `Create Asset` event

The [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164) describes how to use classes and categories to create scriptable apps (referred to as Cocoa scripting) in the Cocoa application framework.

### Review a Scripting Definition Example: Asset Management Suite

An app that interacts with Final Cut Pro must support the events and object classes described in the previous tables. The following code shows a complete example of a scripting definition used by an asset-management app.

```swift
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE dictionary SYSTEM "file://localhost/System/Library/DTDs/sdef.dtd">
 
<!--
 
   File: AssetManagementSuite.sdef
 Abstract: Asset Management suite scripting definitions
     for the SimpleAssetManager sample code.
  Version: 1.6

    Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple Inc. ("Apple") in consideration of your agreement to the following terms, and your use, installation, modification or redistribution of this Apple software constitutes acceptance of these terms.  If you do not agree with these terms, please do not use, install, modify or redistribute this Apple software.
    In consideration of your agreement to abide by the following terms, and subject to these terms, Apple grants you a personal, non-exclusive license, under Apple's copyrights in this original Apple software (the "Apple Software"), to use, reproduce, modify and redistribute the AppleSoftware, with or without modifications, in source and/or binary forms; provided that if you redistribute the Apple Software in its entirety and without modifications, you must retain this notice and the following text and disclaimers in all such redistributions of the Apple Software.
    Neither the name, trademarks, service marks or logos of Apple Inc. may be used to endorse or promote products derived from the Apple Software without specific prior written permission from Apple.  Except as expressly stated in this notice, no other rights or licenses, express or implied, are granted by Apple herein, including but not limited to any patent rights that may be infringed by your derivative works or by other works in which the Apple Software may be incorporated.
    The Apple Software is provided by Apple on an "AS IS" basis.  APPLE MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.
    IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION, MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE), STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (C) 2011-2019 Apple Inc. All Rights Reserved.
 
-->
 
 
<!-- declare the namespace for using XInclude so you can include the standard suite -->
<dictionary xmlns:xi="http://www.w3.org/2003/XInclude">
 
  <!-- use XInclude to include the standard suite -->
  <xi:include href="file:///System/Library/ScriptingDefinitions/CocoaStandard.sdef" xpointer="xpointer(/dictionary/suite)"/>
 
  <!-- specific suite(s) for the application follow... -->
  <suite name="ProVideo Asset Management" code="pvam" description="Scripting terminology for Pro Video Asset Management applications.">
 
    <record-type name="asset location" code="aslc">
      <access-group identifier="com.apple.proapps.assetmanagement.import" access="rw"/>
      <property name="folder" code="asfd" type="file" description="Directory in which the asset files exist.">
        <cocoa key="folder"/>
      </property>
      <property name="base name" code="asbn" type="text" description="Base file name of the asset files.">
        <cocoa key="basename"/>
      </property>
      <property name="has media" code="ashm" type="boolean" description="Whether the asset has rendered media">
        <cocoa key="hasMedia"/>
      </property>
      <property name="has description" code="ashd" type="boolean" description="Whether the asset has an XML description">
        <cocoa key="hasDescription"/>
      </property>
    </record-type>
 
    <!-- record type for library access -->
    <record-type name="library location" code="lblc">
      <access-group identifier="com.apple.proapps.assetmanagement.import" access="rw"/>
      <property name="library folder" code="lbfd" type="file" description="Directory in which the library files exist.">
        <cocoa key="folder"/>
      </property>
      <property name="library base name" code="lbbn" type="text" description="Base file name of the library files.">
        <cocoa key="basename"/>
      </property>
      <property name="has archive" code="lbha" type="boolean" description="Whether the library has data for archive.">
        <cocoa key="hasArchive"/>
      </property>
      <property name="has library description" code="lbhd" type="boolean" description="Whether the library has an XML description.">
        <cocoa key="hasDescription"/>
      </property>
    </record-type>
 
    <value-type name="user defined record" code="usrf">
      <cocoa class="NSDictionary"/>
    </value-type>
 
    <command name="open" code="aevtodoc" description="Open a document.">
      <access-group identifier="com.apple.proapps.assetmanagement.import" access="rw"/>
      <direct-parameter description="The file(s) to be opened.">
        <type type="file"/>
        <type type="file" list="yes"/>
      </direct-parameter>
      <result description="The opened document(s).">
        <type type="document"/>
        <type type="document" list="yes"/>
      </result>
    </command>
 
    <command name="make" code="corecrel" description="Create a new object.">
      <access-group identifier="com.apple.proapps.assetmanagement.import" access="rw"/>
      <cocoa class="SAMMakeCommand"/>
      <parameter name="new" code="kocl" type="type" description="The class of the new object.">
        <cocoa key="ObjectClass"/>
      </parameter>
      <parameter name="at" code="insh" type="location specifier" optional="yes" description="The location at which to insert the object.">
        <cocoa key="Location"/>
      </parameter>
      <parameter name="with data" code="data" type="any" optional="yes" description="The initial contents of the object.">
        <cocoa key="ObjectData"/>
      </parameter>
      <parameter name="with properties" code="prdt" type="record" optional="yes" description="The initial values for properties of the object.">
        <cocoa key="KeyDictionary"/>
      </parameter>
      <result type="specifier" description="The new object."/>
    </command>
 
    <class-extension name="application" extends="application">
      <access-group identifier="com.apple.proapps.assetmanagement.import" access="rw"/>
      <cocoa class="NSApplication"/>
      <property name="name" code="pnam" type="text" access="r" description="The name of the application.">
        <access-group identifier="com.apple.proapps.assetmanagement.import" access="rw"/>
      </property>
      <element type="document">
        <access-group identifier="com.apple.proapps.assetmanagement.import" access="rw"/>
      </element>
    </class-extension>
 
    <class name="document" code="docu" description="A document." inherits="document">
      <access-group identifier="com.apple.proapps.assetmanagement.import" access="rw"/>
      <cocoa class="SAMDocument"/>
      <property name="name" code="pnam" type="text" access="r" description="The name of the application.">
        <access-group identifier="com.apple.assetmanagement.import" access="rw"/>
      </property>
      <property name="id" code="ID  " type="text" access="r" description="The unique identifier of the asset">
        <access-group identifier="com.apple.assetmanagement.import" access="rw"/>
      </property>
      <element type="asset">
        <access-group identifier="com.apple.assetmanagement.import" access="rw"/>
        <cocoa key="assets"/>
      </element>
    </class>
 
    <class name="asset" code="aset" description="A media asset.">
      <access-group identifier="com.apple.assetmanagement.import" access="rw"/>
      <cocoa class="SAMAsset"/>
      <property name="id" code="ID  " type="text" access="r" description="The unique identifier of the asset">
        <access-group identifier="com.apple.assetmanagement.import" access="rw"/>
        <cocoa key="uniqueID"/>
      </property>
      <property name="name" code="pnam" type="text" access="r" description="Its name.">
        <access-group identifier="com.apple.assetmanagement.import" access="rw"/>
        <cocoa key="name"/>
      </property>
      <property name="location info" code="locn" type="asset location" access="r" description="Location information of the asset.">
        <access-group identifier="com.apple.assetmanagement.import" access="rw"/>
        <cocoa key="locationInfo"/>
      </property>
      <property name="library info" code="lbry" type="library location" access="r" description="Location information of the containing library in the source.">
        <access-group identifier="com.apple.assetmanagement.import" access="rw"/>
        <cocoa key="libraryInfo"/>
      </property>
      <property name="metadata" code="meta" type="user defined record" access="rw" description="Metadata associated to the asset.">
        <access-group identifier="com.apple.assetmanagement.import" access="rw"/>
        <cocoa key="metadata"/>
      </property>
      <property name="data options" code="dopt" type="user defined record" access="rw" description="Data creation options for the asset.">
        <access-group identifier="com.apple.assetmanagement.import" access="rw"/>
        <cocoa key="dataOptions"/>
      </property>
    </class>
    <enumeration name="saveable file format" code="savf">
      <enumerator name="document" code="docu" description="A document."/>
    </enumeration>
  </suite>
</dictionary>

```

## See Also

### Handling Apple Events
- [Responding to Apple Events from Final Cut Pro](./responding-to-apple-events-from-final-cut-pro.md)
  Tell Final Cut Pro about the kind of data your users want to receive in your app through a custom share destination.
- [Supporting Conversions with Scripting Class Extensions](./supporting-conversions-with-scripting-class-extensions.md)
  Support conversions between the Apple event descriptor types and Foundation object classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/creating-scripting-definitions-for-custom-share-destinations)*