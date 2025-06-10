# Configuring Multiple Devices Using Profiles

**Framework**: Device Management

Create and deploy configuration profiles to users within your organization.

#### Overview

Configuration profiles streamline the process of setting up a large number of devices. Custom calendar and email settings, network settings (like WiFi and VPN settings), certificates, and device restrictions, are some of the properties you can configure using configuration profiles.

You have several options for deploying configuration profiles:

- Using Apple Configurator 2, available in the App Store.
- In an email message.
- On a webpage.
- Using over-the-air configuration as described in [`Over-the-Air Profile Delivery and Configuration`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/iPhoneOTAConfiguration/Introduction/Introduction.html).
- Over the air using a Mobile Device Management server.

> ❗ **Important**:  Configuration profiles are for enterprise use only. With the exceptions of the APN, VPN, and WiFi profiles, don’t use configuration profiles with consumer apps.

##### Define a Profile

Configuration profiles are in a property list format, which any XML tool can read and write.

The configuration property list contains the properties listed in the [`TopLevel`](toplevel.md) object. These properties describe the profile and the rules for deploying it. Specific configuration values are stored in an array of payloads in the `PayloadContent` property.

Each payload’s contents contain profile-specific keys (see [`Profile-Specific Payload Keys`](profile-specific-payload-keys.md)) and keys that are common to all payloads (see the following list of key definitions).

##### Encrypt and Sign a Profile

Both iOS and macOS support using encryption to protect the contents of profiles from unauthorized access. The encrypted profile can only be decrypted using a private key previously installed on a device. To encrypt a profile:

1. Remove the `PayloadContent` array and serialize it as a property list. Note that the top-level object in this property list is an array, not a dictionary.
2. CMS-encrypt the serialized property list as enveloped data.
3. Serialize the encrypted data in DER (Distinguished Encoding Rules) format.
4. Set the serialized data as the value of as a data property list item in the profile, using the `EncryptedPayloadContent` key.

Signing a profile guarantees data integrity. To sign a profile, place the XML property list in a DER-encoded, CMS Signed Data structure. When replacing a signed configuration profile, if you don’t sign the replacement using the exact same signing identity, the device rejects the replacement, unless installing the replacement through MDM or OTA.

##### Example Scep Configuration Profile

The listing below shows the contents of an example profile, containing a Simple Certificate Enrollment Protocol (SCEP) payload.

```other
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple Inc//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
   <dict>
      <key>PayloadVersion</key>
      <integer>1</integer>
      <key>PayloadUUID</key>
      <string>Ignored</string>
      <key>PayloadType</key>
      <string>Configuration</string>
      <key>PayloadIdentifier</key>
      <string>Ignored</string>
      <key>PayloadContent</key>
      <array>
         <dict>
            <key>PayloadContent</key>
            <dict>
               <key>URL</key> 
               <string>https://scep.example.com/scep</string> 
               <key>Name</key> 
               <string>EnrollmentCAInstance</string> 
               <key>Subject</key>
               <array> 
                  <array> 
                     <array>
                        <string>O</string>
                        <string>Example, Inc.</string>
                     </array>
                  </array>
                  <array>
                     <array>
                        <string>CN</string>
                        <string>User Device Cert</string>
                     </array>
                  </array>
               </array>
               <key>Challenge</key>
               <string>...</string>
               <key>Keysize</key>
               <integer>1024</integer>
               <key>KeyType</key>
               <string>RSA</string>
               <key>KeyUsage</key>
               <integer>5</integer>
            </dict>
            <key>PayloadDescription</key>
            <string>Provides device encryption identity</string> 
            <key>PayloadUUID</key> 
            <string>fd8a6b9e-0fed-406f-9571-8ec98722b713</string> 
            <key>PayloadType</key> 
            <string>com.apple.security.scep</string> 
            <key>PayloadDisplayName</key> 
            <string>Encryption Identity</string> 
            <key>PayloadVersion</key> 
            <integer>1</integer> 
            <key>PayloadOrganization</key> 
            <string>Example, Inc.</string> 
            <key>PayloadIdentifier</key> 
            <string>com.example.profileservice.scep</string> 
         </dict>
      </array>
   </dict>
</plist>

```

## See Also

- [Profile-Specific Payload Keys](profile-specific-payload-keys.md)
  Use the appropriate payload for your configuration needs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/configuring-multiple-devices-using-profiles)*