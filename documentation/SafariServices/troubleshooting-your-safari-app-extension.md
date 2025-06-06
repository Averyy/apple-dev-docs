# Troubleshooting your Safari app extension

**Framework**: Safari Services

Debug your Safari app extension with these techniques.

#### Overview

Here are a few options for debugging your Safari app extension:

 Make sure your website access permissions and allowed domain patterns are right. For more details, see [`Adjusting website access permissions`](adjusting-website-access-permissions.md).

 Make sure your URL patterns are right. For more details, see [`Specify URL patterns`](using-permissions-for-scripts-and-style-sheets#Specify-URL-patterns.md).

 Check that the deployment target for your app is set to the system you are testing on.

 In the Terminal app, type the following command:

```swift
pluginkit -mAvvv -p com.apple.Safari.extension
```

 In the JavaScript environment, use the console.log command to print messages to the Safari debugging console:

```swift
console.log("injection script on " + document.location.href);
```

 In the native environment, calls to `NSLog` or `print` from within your Safari app extension are sent to the system console and are visible in the Console app. You can also filter for other messages using the name of your app extension. For example, if your app extension is terminated because of an error, a message is sent to the Console and a crash log is generated.

 Many Safari app extensions provide a standalone experience that’s completely independent of the containing app. In other cases, the reason for providing the Safari app extension is to integrate content from your app into the Safari web experience. To integrate content, you need to share information between your app and app extension, and to do so, you need to ensure that your extension is enabled. For security reasons, when your app is installed on a system, its Safari app extensions aren’t automatically enabled; the end user must explicitly enable each extension. Use your app to check to see whether one of its app extensions has been enabled and, if necessary, display the app extension’s Safari settings panel so the end user can enable it.

## See Also

- [Building a Safari app extension](building-a-safari-app-extension.md)
  Add, build, and enable a Safari app extension.
- [Converting a legacy Safari extension to a Safari app extension](converting-a-legacy-safari-extension-to-a-safari-app-extension.md)
  Convert a legacy Safari extension to a Safari app extension, automatically with keys or manually.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/troubleshooting-your-safari-app-extension)*