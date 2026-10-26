# Building an Encoder Extension

**Framework**: Professional-Video-Applications  
**Role**: Article

Create an encoder extension in Xcode by using the Encoder Extension template.

#### Overview

When you want to integrate a custom output file format into the Compressor export settings to allow users to export their Final Cut Pro projects to that format, consider creating an encoder extension. You add and configure an encoder extension as a separate target alongside a macOS app. If you don’t have a functional macOS app, create an empty one to contain the encoder extension. The app that contains your extension is called the *container app*.

Use the Xcode template project that comes with the Compressor Extension SDK as a starting point to create your encoder extension.

##### Install the Compressor Extension SDK

Download and install the Compressor Extension SDK from [Apple’s developer website](https://developer.apple.com/download/all/?q=Encoder).

Run the installer that comes with the Compressor Extension SDK. It installs the Xcode template in the appropriate locations on your computer.

##### Add an Encoder Extension Target to Your Project

To add an encoder extension target to your macOS app:

1. Launch Xcode and open your existing macOS app project.
2. Choose File > New > Target.
3. From the Xcode template window (shown in the illustration below), choose the macOS tab, select the Encoder Extension template from the Compressor Encoder Extension section, and click Next.
4. Enter a product name for your extension and set other options, like your organization name.
5. Make sure that you select your app project in the Project menu, and your macOS app target in the Embed in Application menu.
6. Click Finish.

![Screenshot showing the Encoder Extension template location in the Xcode template window.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3646158@2x.png)

The Xcode template sets up relevant build options and creates an initial set of project files for the encoder extension. The initial set of files includes an `Info.plist` file, and default source files for an encoder extension.

The Xcode template configures the `Info.plist` file in your initial project with the default information about your extension capabilities, and identifies your extension as a Compressor app encoder extension. In most cases, you don’t need to modify this file. For an explanation of the available keys and values, see the Information Property List Keys.

##### Build and Run Your Project

To ensure that the system can find and register your extension for use within the Compressor app interface, build and run your project. In the Xcode Editor toolbar, click the Run button (►), or choose Product > Run (Command-R).

During the build process, Xcode inserts the extension in the proper place in your app bundle, and you get an encoder extension bundle (ending in `.appex`) that runs in its own process, independent of the container app. When Xcode completes the build, it launches the container app.

To customize your extension, modify the target’s source and resource file as you like, and recompile. 

> **Note**:  Launching the container app once registers your extension as an available encoder extension for the Compressor app.

##### Debug Your Encoder Extension

After the build and run process is complete, the Compressor app makes your extension available in its interface. To view your extension, launch the Compressor app. In the Settings pane, click the Add pop-up menu and select New Setting. The new extension should now be visible in the Format menu of the dialog that appears.

You can connect the Xcode debugger to an encoder extension process after launching the extension. Note that several extension processes may be associated with the Compressor app.  Use the activity monitor to find the process you want to debug, and attach the Xcode debugger to it.

Avoid using a distributed encoder cluster while debugging. In a distributed processing environment, the Compressor app randomly assigns an encoding job to an available extension process, and you won’t know in advance which extension process receives which encoder job. With a single encoder instance, the Compressor app assigns all work to that encoder instance, and you can debug in a single process.

To attach the Xcode debugger after launching the extension:

1. Invoke the extension from the Compressor app interface.
2. From the Xcode menu, choose Debug > Attach to Process, then select the extension by name or from the list of running processes.

The Xcode debugger attaches to the extension’s process, sets active breakpoints, and lets the extension execute. At this point, you can use the same Xcode debugging features you use to debug other processes.

##### Distribute Your Extension

To distribute your encoder extension to users, submit the container app to the App Store. When a user installs the containing app, the extension it contains is installed and becomes available in the Compressor interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/building-an-encoder-extension)*