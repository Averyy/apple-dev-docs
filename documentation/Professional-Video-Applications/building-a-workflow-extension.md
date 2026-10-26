# Building a Workflow Extension

**Framework**: Professional-Video-Applications  
**Role**: Article

Create a workflow extension in Xcode by using the Final Cut Pro Workflow Extension template.

#### Overview

When you are ready to develop a workflow extension, build it using the Xcode template that comes with the Workflow Extension SDK. The Xcode template packages the extension code in a specific manner (`.appex`) and embeds it in an app bundle. When a user installs the app containing your extension, macOS registers the workflow extension, and Final Cut Pro makes the extension available in its interface.

##### Install the Workflow Extension SDK

Download and install the Workflow Extension SDK from [Apple’s developer website](https://developer.apple.com/download/all/?q=WorkflowExtensions).

Run the installer that comes with the Workflow Extension SDK. It installs the relevant frameworks and the Xcode template in the appropriate locations on your computer.

##### Add a Workflow Extension Target to Your Project

You create and configure the workflow extension as a separate target alongside your app. Start by launching Xcode and opening your existing macOS app project. Then choose File > New > Target, select the Final Cut Pro Workflow Extension template from the Workflow Extension section of the macOS platform, and click Next, as shown in the following image.

![Screenshot showing the Final Cut Pro Workflow Extension template location in the Xcode template window.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3562763@2x.png)

Enter a product name for your extension and set other options, like your organization name. Make sure that your app project is selected in the Project menu, and that your macOS app target is selected in the Embed in Application menu. Then click Finish.

The Xcode template sets up relevant build options and creates an initial set of project files for the workflow extension. A workflow extension template includes an `Info.plist` file, a view controller class, and a default user interface. With this initial set of files, you can build and run the project even before you customize the workflow extension code. During the build process, Xcode inserts the extension in the proper place in your app bundle, and you get a workflow extension bundle (ending in `.appex`) that runs in its own process.

##### Add Keys to the Info Property List Template

The default `Info.plist` file identifies your workflow extension and may specify some details about your extension under the `NSExtension` key.

```other
  <key>NSExtension</key>
  <dict>
    <key>NSExtensionPointIdentifier</key>
    <string>com.apple.FinalCut.WorkfloWExtension</string>
    <key>ProExtensionPrincipalViewControllerClass</key>
    <string>MyExtensionViewController</string>
  </dict>
```

Also, if required, you can add keys to the `Info.plist` file to specify the minimum size of the floating window in which Final Cut Pro displays a workflow extension view.

For example, to limit the minimum size of the floating window to 100 x 100 pixels, add the following values to the `Info.plist` file under the `ProExtensionAttributes` key.

```other
  <key>ProExtensionAttributes</key>
  <dict>
    <key>ContentViewMinimumWidth</key>
    <integer>100</integer>
    <key>ContentViewMinimumHeight</key>
    <integer>100</integer>
  </dict>
```

For more information, see [Set a Minimum Floating Window Size](./designing-workflow-extensions.md#Set-a-Minimum-Floating-Window-Size).

##### Modify the Workflow Extension Principal Class

A workflow extension is essentially a view controller class for the view hosted in the Final Cut Pro interface. The Xcode template provides a subclass of `NSViewController`, which is the principal class that serves as the primary view controller of the workflow extension. When Final Cut Pro  (the host app) invokes your extension, an operating system service instantiates this class.

The principal class has stubs for methods you can modify to customize the workflow in your extension. You can modify this class to act as an observer for changes in the Final Cut Pro timeline or to add support for drag and drop functionality.

When a user closes an extension’s floating window, the view controller invokes the [`viewWillDisappear()`](../AppKit/nsviewcontroller/viewwilldisappear%28%29.md) method of your extension’s principal class, and the view disappears from the window. Override the `viewWillDisappear` method to remove references to objects that you no longer need or anything you need to do when the view disappears. For example, you may use this method to stop an audio session or to manage any custom objects in your extension.

##### Enable and Verify Your Workflow Extension

To test your workflow extension before submitting it to the app store, you must enable it by installing the containing app in your `/Application` folder and launching the app once from there. This step makes Final Cut Pro recognize and display your extension in its interface.

To verify that your extension is available in Final Cut Pro, check the extension menu to see if it appears in the list of available extensions. Each menu item contains the localized name of the extension along with the extension icon. You can also get the list of available extensions from the  Extensions item in the Window menu. Either way, when a user chooses an extension, Final Cut Pro loads it and displays its interface.

> **Note**:  Final Cut Pro displays an extension menu in its toolbar only if it has available workflow extensions.

##### Debug Your Workflow Extension

Debugging your workflow extension in Xcode is similar to debugging any other process in an Xcode debugger. You can connect the Xcode debugger to a workflow extension process before or after launching a workflow extension.

To connect the Xcode debugger before launching an extension, you attach the debugger to the extension by its name. Choose the Attach to Process by PID or Name option from the Xcode Debug menu.

To attach the Xcode debugger after launching the extension:

1. Invoke the extension from the Final Cut Pro interface.
2. From the Xcode menu, choose Debug > Attach to Process, then select the extension by name or from the list of running processes.

The Xcode debugger attaches to the extension’s process, sets active breakpoints, and lets the extension execute. At this point, you can use the same Xcode debugging features that you use to debug other processes.

## See Also

### Essentials
- [Designing Workflow Extensions](./designing-workflow-extensions.md)
  Follow these design guidelines to provide a unique experience to workflow extension users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/building-a-workflow-extension)*