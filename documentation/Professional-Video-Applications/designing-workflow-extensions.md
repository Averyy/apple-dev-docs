# Designing Workflow Extensions

**Framework**: Professional-Video-Applications  
**Role**: Article

Follow these design guidelines to provide a unique experience to workflow extension users.

## Overview

Workflow extensions share many similarities with app extensions. Both are packaged inside your app and use similar design infrastructure for bridging communication and exchanging data with the host app and container app. The key difference is that the extension view remains in a floating window until a user closes it. In contrast, certain app extensions, such as the [Share extension](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/Share.html#//apple_ref/doc/uid/TP40014214-CH12-SW1), usually run as a modal session.

As you create a workflow extension, you may need to take into account some design scenarios that are unique to workflow extensions. Take the following guidelines into account when designing a workflow extension for your app.

### Add Drag and Drop Functionality

To support the frequent exchange of small batches of data back and forth between your extension and Final Cut Pro, add drag and drop functionality. See [Supporting Drag and Drop for Data Sent to Final Cut Pro](./supporting-drag-and-drop-for-data-sent-to-final-cut-pro.md) and [Supporting Drag and Drop to Receive Final Cut Pro Data](./supporting-drag-and-drop-to-receive-final-cut-pro-data.md).

### Receive Rendered Media Through the Containing App

When you have workflows that require your extension to receive rendered media from Final Cut Pro for further processing, receive the rendered sequence in the container app and have the workflow extension access it from there. Unlike an app, a workflow extension cannot receive rendered media directly from Final Cut Pro. You can set up a shared container to access data that is available in the container app. If your extension or container app communicates with a backend server, uploading the data to the backend server allows data sharing between the extension and the container app. See [Sharing Data with Your Containing App](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/ExtensionScenarios.html#//apple_ref/doc/uid/TP40014214-CH21-SW6).

### Share Custom Code with the Containing App

If you have custom code that is common to both your app and your workflow extension, you can share the code between them. Place the shared code in a framework and embed the framework in both targets. See [Using an Embedded Framework to Share Code](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/ExtensionScenarios.html#//apple_ref/doc/uid/TP40014214-CH21-SW5).

### Save the Workflow Extension State

Final Cut Pro terminates a workflow extension soon after a user closes the extension window. When they reopen it, they are likely to expect the state of the extension to be preserved. To maintain the state of your extension, automatically save the state to persistent storage, like an encrypted file or a remote server. You can also set up a shared container with the containing app and save relevant state information in the shared container. See [Sharing Data with Your Containing App](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/ExtensionScenarios.html#//apple_ref/doc/uid/TP40014214-CH21-SW6).

### Add a Logo and an Icon

To deliver a seamless experience when users switch between Final Cut Pro and the extension interface, give the extension interface a look and feel that’s consistent with that of the Final Cut Pro interface. For example, choose Dark Mode for your extension interface to match the  appearance of the Final Cut Pro interface. To help users recognize that the extension view is not part of Final Cut Pro,  add your company logo to the extension view.

Users identify your extension by its icon and name. Creating your extension from the Xcode template adds an asset catalog with empty entries for an icon. Follow the steps outlined in [Create asset catalog and sets](https://help.apple.com/xcode/mac/current/#/dev10510b1f7) to add an icon for your extension. If you don’t provide an icon, Final Cut Pro automatically adds the container app’s icon for the extension.

### Set a Minimum Floating Window Size

The floating window in which Final Cut Pro hosts the workflow extension view is resizable. Often, the UI design of the workflow extension requires a specific window size to properly display the contents of an extension view. You can restrict a user from resizing the floating window smaller than a specific size by specifying a minimum required size for the floating window in your `Info.plist` file. See [Add Keys to the Info Property List Template](./building-a-workflow-extension.md#Add-Keys-to-the-Info-Property-List-Template).

## See Also

### Essentials
- [Building a Workflow Extension](./building-a-workflow-extension.md)
  Create a workflow extension in Xcode by using the Final Cut Pro Workflow Extension template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/designing-workflow-extensions)*