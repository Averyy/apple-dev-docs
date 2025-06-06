# Creating App Clip Codes

**Framework**: App Clips

Help users discover your App Clip by using an NFC-integrated or scan-only App Clip Code.

#### Overview

An App Clip Code is immediately recognizable to users and lets them know an App Clip is available. The App Clip Code offers a fast and secure launch experience for your App Clip that users trust.

![Illustration of two App Clip Codes that use the badge design: On the left, a white-on-blue App Clip Code with an embedded NFC tag. On the right, a scan-only, white-on-black App Clip Code.](https://docs-assets.developer.apple.com/published/d128732b4333996b712930a76efbaf5c/media-3706497%402x.png)

The visual design of an App Clip Code encodes your App Clip’s . Optionally, you can embed an NFC tag that also encodes the invocation URL. An App Clip Code with an embedded NFC tag is called an  App Clip Code, while a code without an NFC tag is called a  App Clip Code.

The image at the center of an App Clip Code icon lets users know how to interact with the code. If they discover an NFC-integrated App Clip Code, they hold their device close to the code or scan it with the NFC Tag Reader in Control Center to launch your App Clip. They can also scan an NFC-integrated App Clip Code with the Camera app or the Code Scanner in Control Center. If they discover a scan-only App Clip Code, they scan it with the Camera or the Code Scanner in Control Center to launch your App Clip.

In addition to providing a great launch experience for your App Clip, you can also use an App Clip Code to offer a context-aware augmented reality experience. For more information, see [`Interacting with App Clip Codes in AR`](interacting-with-app-clip-codes-in-ar.md).

> **Note**:  Scanning App Clip Codes requires a device that runs iOS 14.3 or later.

 Scanning App Clip Codes requires a device that runs iOS 14.3 or later.

Creating an App Clip Code requires the following tasks:

1. Choosing an invocation URL and configuring an  in [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com/login). To learn more, see [`Configuring the launch experience of your App Clip`](configuring-the-launch-experience-of-your-app-clip.md).
2. Choosing the type (scan-only or NFC-integrated), colors, and design of your App Clip Code. For design guidance, see [`Human Interface Guidelines > App Clips > App Clip Codes`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/app-clips/overview/app-clip-codes/).
3. Generating App Clip Codes with App Store Connect or with the App Clip Code Generator command-line tool. For more information, see [`Pick a tool to create App Clip Codes`](creating-app-clip-codes#Pick-a-tool-to-create-App-Clip-Codes.md) below.
4. Printing App Clip Codes yourself or with the help of a professional printing service — for example, [`RR Donnelley`](https://developer.apple.comhttps://touchless.acc.rrd.com/). For printing guidance, see [`Human Interface Guidelines > App Clips > Printing Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/app-clips/overview/printing-guidelines/) and [`Preparing multiple App Clip Codes for production`](preparing-multiple-app-clip-codes-for-production.md).

For more information, see [`Encoding a URL in an App Clip Code`](encoding-a-url-in-an-app-clip-code.md).

##### Pick a Tool to Create App Clip Codes

App Clip Codes always use the design Apple provides to ensure users instantly recognize them. You can create an App Clip Code by selecting an advanced App Clip experience in [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com/login) or by installing the [`App Clip Code Generator`](https://developer.apple.comhttps://developer.apple.com/app-clips/resources/) command-line tool. Both have similar features and it’s up to you to pick the tool that best fits your needs.

Consider using App Store Connect if:

- You’ve already created an advanced App Clip experience in App Store Connect.
- You prefer an instantaneous preview while you experiment with colors.
- You’re comfortable using a tool that offers a more visual interface compared to a command-line tool.

Consider using the App Clip Code Generator command-line tool if:

- You haven’t created an advanced App Clip experience in App Store Connect — for example, during development of your App Clip.
- You need to create a lot of App Clip Codes and want to automate their creation with a script.
- You’re comfortable using a command-line tool.

For more information, see [`Creating App Clip Codes with App Store Connect`](creating-app-clip-codes-with-app-store-connect.md) and [`Creating App Clip Codes with the App Clip Code Generator`](creating-app-clip-codes-with-the-app-clip-code-generator.md).

> **Note**:  You must be enrolled in the Apple Developer Program before you can download the App Clip Code Generator. For information about the Apple Developer Program, see [`How the Program Works`](https://developer.apple.comhttps://developer.apple.com/programs/how-it-works/).

 You must be enrolled in the Apple Developer Program before you can download the App Clip Code Generator. For information about the Apple Developer Program, see [`How the Program Works`](https://developer.apple.comhttps://developer.apple.com/programs/how-it-works/).

## See Also

- [Preparing multiple App Clip Codes for production](preparing-multiple-app-clip-codes-for-production.md)
  Prepare your App Clip Codes to send to a professional printing service.
- [Interacting with App Clip Codes in AR](interacting-with-app-clip-codes-in-ar.md)
  Display content and provide services in an AR experience with App Clip Codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appclip/creating-app-clip-codes)*