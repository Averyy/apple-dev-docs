# Creating a Message Filter App Extension

**Framework**: SMS and Call Reporting

Create an app extension that helps identify unwanted messages.

#### Overview

To create a Message Filter app extension, add a target that uses the Message Filter Extension template to the Xcode project for your containing app. The principal view controller in your app extension is a subclass of [`ILMessageFilterExtension`](ilmessagefilterextension.md) that adopts the [`ILMessageFilterQueryHandling`](ilmessagefilterqueryhandling.md) protocol.

If you have servers that can help your app extension determine how to handle a message, you must add the Associated Domains capability to your Xcode project and specify those domains. Then, you must set up shared credentials as described in [`Shared Web Credentials`](https://developer.apple.com/documentation/Security/shared-web-credentials), substituting `messagefilter` for `webcredentials` throughout the steps. Lastly, you must specify the domains in your `Info.plist` file, which should look similar to the dictionary shown below.

```xml
<key>NSExtension</key>
    <dict>
        <key>NSExtensionPrincipalClass</key>
            <string>MessageFilterExtension</string>
        <key>NSExtensionAttributes</key>
            <dict>
                <key>ILMessageFilterExtensionNetworkURL</key>
                <string>https://www.example-sms-filter-application.com/api</string>
            </dict>
        <key>NSExtensionPointIdentifier</key>
        <string>com.apple.identitylookup.message-filter</string>
     </dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/creating-a-message-filter-app-extension)*