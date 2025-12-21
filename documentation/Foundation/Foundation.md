# Foundation

**Framework**: Foundation  
**Kind**: module

Access essential data types, collections, and operating-system services to define the base layer of functionality for your app.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

#### Overview

The Foundation framework provides a base layer of functionality for apps and frameworks, including data storage and persistence, text processing, date and time calculations, sorting and filtering, and networking. The classes, protocols, and data types defined by Foundation are used throughout the macOS, iOS, watchOS, and tvOS SDKs.

## Topics

### Fundamentals
- [Numbers, Data, and Basic Values](numbers-data-and-basic-values.md)
  Work with primitive values and other fundamental types used throughout Cocoa.
- [Strings and Text](strings-and-text.md)
  Create and process strings of Unicode characters, use regular expressions to find patterns, and perform natural language analysis of text.
- [Collections](collections.md)
  Use arrays, dictionaries, sets, and specialized collections to store and iterate groups of objects or values.
- [Dates and Times](dates-and-times.md)
  Compare dates and times, and perform calendar and time zone calculations.
- [Units and Measurement](units-and-measurement.md)
  Label numeric quantities with physical dimensions to allow locale-aware formatting and conversion between related units.
- [Data Formatting](data-formatting.md)
  Convert numbers, dates, measurements, and other values to and from locale-aware string representations.
- [Filters and Sorting](filters-and-sorting.md)
  Use predicates, expressions, and sort descriptors to examine elements in collections and other services.
### App Support
- [Task Management](task-management.md)
  Manage your app’s work and how it interacts with system services like Handoff and Shortcuts.
- [Resources](resources.md)
  Access assets and other data bundled with your app.
- [Notifications](notifications.md)
  Design patterns for broadcasting information and for subscribing to broadcasts.
- [App Extension Support](app-extension-support.md)
  Manage the interaction between an app extension and its hosting app.
- [Errors and Exceptions](errors-and-exceptions.md)
  Respond to problem situations in your interactions with APIs, and fine-tune your app for better debugging.
- [Scripting Support](scripting-support.md)
  Allow users to control your app with AppleScript and other automation technologies, or run scripts from within your app.
### Files and Data Persistence
- [File System](file-system.md)
  Create, read, write, and examine files and folders in the file system.
- [Archives and Serialization](archives-and-serialization.md)
  Convert objects and values to and from property list, JSON, and other flat binary representations.
- [Settings](settings.md)
  Configure your app using data you store persistently on the local disk or in iCloud.
- [Spotlight](spotlight.md)
  Search for files and other items on the local device, and index your app’s content for searching.
- [iCloud](icloud.md)
  Manage files and key-value data that automatically synchronize among a user’s iCloud devices.
- [Optimizing Your App’s Data for iCloud Backup](optimizing-your-app-s-data-for-icloud-backup.md)
  Minimize the space and time that backups take to create by excluding purgeable and nonpurgeable data from backups.
### Networking
- [URL Loading System](url-loading-system.md)
  Interact with URLs and communicate with servers using standard Internet protocols.
- [Bonjour](bonjour.md)
  Advertise services for easy discovery on local networks, or discover services advertised by others.
### Low-Level Utilities
- [XPC](xpc.md)
  Manage secure interprocess communication.
- [Object Runtime](object-runtime.md)
  Get low-level support for basic Objective-C features, Cocoa design patterns, and Swift integration.
- [Processes and Threads](processes-and-threads.md)
  Manage your app’s interaction with the host operating system and other processes, and implement low-level concurrency features.
- [Streams, Sockets, and Ports](streams-sockets-and-ports.md)
  Use low-level Unix features to manage input and output among files, processes, and the network.
### Reference
- [Foundation Enumerations](foundation-enumerations.md)
- [Foundation Data Types](foundation-data-types.md)
  This document describes the data types and constants found in the Foundation framework.
### Articles
- [allocWithZone:](1807189-allocwithzone.md)
  Returns an instance of the `NSMachPort` class.
- [init](1808546-init.md)
  Returns an initialized `NSOperation` object.
- [initWithCoefficient:constant](1864803-initwithcoefficient.md)
  Initializes the unit converter with the coefficient and constant you specify.
- [intersectSet:](1807012-intersectset.md)
  Removes from the receiving set each object that isn’t a member of another given set.
- [isEqual:](1806686-isequal.md)
  Returns a Boolean value that indicates whether the receiver and a given object have identical URL strings and base URLs.
- [minusSet:](1807010-minusset.md)
  Removes each object in another given set from the receiving set, if present.
- [NSJavaBundleCleanup](1806670-nsjavabundlecleanup.md)
  This function has been deprecated.
- [NSJavaBundleSetup](1806677-nsjavabundlesetup.md)
  This function has been deprecated.
- [NSJavaClassesForBundle](1806687-nsjavaclassesforbundle.md)
  Loads the Java classes located in the specified bundle.
- [NSJavaClassesFromPath](1806697-nsjavaclassesfrompath.md)
  Loads the Java classes located at the specified path.
- [NSJavaDidCreateVirtualMachineNotification](nsjavadidcreatevirtualmachinenotification.md)
  Notification sent after the Java virtual machine is created.
- [NSJavaDidSetupVirtualMachineNotification](nsjavadidsetupvirtualmachinenotification.md)
  Notification sent after the Java virtual machine is set up.
- [NSJavaNeedsToLoadClasses](1806703-nsjavaneedstoloadclasses.md)
  Returns a Boolean value that indicates whether a virtual machine is needed or if Java classes are provided.
- [NSJavaNeedsVirtualMachine](1806712-nsjavaneedsvirtualmachine.md)
  Returns a Boolean value that indicates whether a Java virtual machine is required.
- [NSJavaObjectNamedInPath](1806720-nsjavaobjectnamedinpath.md)
  Creates an instance of the named class using the class loader previously specified at the given path.
- [NSJavaProvidesClasses](1806727-nsjavaprovidesclasses.md)
  Returns a Boolean value that indicates whether Java classes are provided.
- [NSJavaSetup](1806733-nsjavasetup.md)
  Loads the Java virtual machine with specified parameters.
- [NSJavaSetupVirtualMachine](1806737-nsjavasetupvirtualmachine.md)
  Sets up the Java virtual machine.
- [NSJavaWillCreateVirtualMachineNotification](nsjavawillcreatevirtualmachinenotification.md)
  Notification sent before the Java virtual machine is created.
- [NSJavaWillSetupVirtualMachineNotification](nsjavawillsetupvirtualmachinenotification.md)
  Notification sent before the Java virtual machine is set up.
- [NSLocaleSensitivePredicateOption](nslocalesensitivepredicateoption.md)
  Indicates that strings to be compared using `<`, `<=`, `=`, `=>`, `>` should be handled in a locale-aware fashion.
- [NSMaxXEdge](nsmaxxedge.md)
  The maximum X edge. This is equivalent to [`CGRectEdge.maxXEdge`](https://developer.apple.com/documentation/CoreFoundation/CGRectEdge/maxXEdge).
- [NSMaxYEdge](nsmaxyedge.md)
  The maximum X edge. This is equivalent to [`CGRectEdge.maxXEdge`](https://developer.apple.com/documentation/CoreFoundation/CGRectEdge/maxXEdge).
- [NSMinXEdge](nsminxedge.md)
  The minimum X edge. This is equivalent to [`CGRectEdge.minXEdge`](https://developer.apple.com/documentation/CoreFoundation/CGRectEdge/minXEdge).
- [NSMinYEdge](nsminyedge.md)
  The minimum Y edge. This is equivalent to [`CGRectEdge.minYEdge`](https://developer.apple.com/documentation/CoreFoundation/CGRectEdge/minYEdge).
- [objCType](1807278-objctype.md)
  Returns a C string containing the Objective-C type of the data contained in the number object.
- [setURI:](1806643-seturi.md)
  Sets the URI of the receiver.
- [unionSet:](1807006-unionset.md)
  Adds each object in another given set to the receiving set, if not present.
### Structures
- [struct DiscontiguousAttributedSubstring](discontiguousattributedsubstring.md)
  A discontiguous portion of an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Foundation)*