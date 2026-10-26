# Building an FxPlug plug-in from an Xcode template

**Framework**: Professional-Video-Applications  
**Role**: Article

Create a plug-in in Xcode with the FxPlug template.

#### Overview

When you run the FxPlug installation bundle, it makes an FxPlug Xcode template available in Xcode. The template’s application bundle contains preconfigured interfaces, source code files, and a Metal renderer that you can use to create a basic filter plug-in for adjusting brightness with Swift or Objective-C. Once you have the brightness plug-in working, you can modify it to make your own plug-in that serves your specific needs.

> **Note**:  To set up your Mac to develop for FxPlug, see [Setting up for FxPlug development](./setting-up-for-fxplug-development.md).

##### Create a basic plug-in from the Xcode template

Begin by launching Xcode and choosing “Create a new Xcode project,” then select the FxPlug 4 template.

1. In the template window, select the macOS category, then find and select the FxPlug 4 template, and click Next.

![A screenshot showing the FxPlug 4 template icon location in the Xcode template window.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-4295739@2x.png) 2. Enter a Product Name (for example, MyPlug-in) for your plug-in, choose None for Team, and set any other options like your organization ID, for example `com.mycompany`. Choose Objective-C or Swift, and click Next.

![A screenshot showing the FxPlug plug-in options for the new project.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-4295737@2x.png) 3. Specify a location for your project and click Create. The template creates a brightness filter FxPlug plug-in project. If the option to create a Git repository on your Mac is not available, click Show Options.

![A screenshot showing the Create screen with the option to create a Git repository on your Mac.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3917573@2x.png) 4. In the Xcode Editor toolbar, check that “Wrapper Application” is the selected scheme, then click the build and run button (►).

![A screenshot showing the build and run button and the scheme selection pop-up.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-4295738@2x.png)

This step ensures that your development environment is set up for FxPlug development, and that macOS can find and register your plug-in for use with Motion and Final Cut Pro. Once Xcode successfully completes the build, it launches the plug-in’s wrapper application. Confirm that the name you gave to your plug-in in step 2 appears in the app’s title bar.

> 💡 **Tip**:  Quit the app you just created. Your plug-in app doesn’t need to be active for it to be discovered by the host application. You only need to launch it once to be registered by macOS as an available FxPlug plug-in.

##### Try out your plug-in with Motion

Once you’ve successfully built and run the template plug-in, apply it to a Motion project to see it in effect.

1. Launch Motion and create a new project in the Project Browser, or select File > New.
2. Add content to your Motion project. The template plug-in is a filter, so you need to apply it to some content. In the Library pane, click Generators, and then choose Checkerboard. Drag the Checkerboard generator to Motion’s canvas.
3. With your Checkerboard generator from step 2 still selected, apply your newly created plug-in. To do this, go to Motion’s Library, choose Filters, search for the name of the filter you built with Xcode, select it, and then click Apply.
4. Test the plug-in’s parameters. In the Inspector pane you’ll see your filter in the Filters pane and its available parameters. Adjust the Brightness parameter to see the effect on the image in the canvas.

![A Motion app screenshot showing a template plug-in applied to a checkerboard generator. The Filters tab is selected in the Inspector pane.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3915699@2x.png)

To customize your plug-in, modify the Xcode project as you wish, and recompile. You’ll need to relaunch any host apps to ensure any changes to your plug-in are loaded.

## See Also

### Plug-in fundamentals
- [Building an FxPlug plug-in manually](./building-an-fxplug-plug-in-manually.md)
  Create your own plug-in in Xcode.
- [Using FxPlug APIs](./using-fxplug-apis.md)
  Use various FxPlug APIs to communicate with host apps like Motion or Final Cut Pro.
- [Editing property lists for FxPlug plug-ins](./editing-property-lists-for-fxplug-plug-ins.md)
  Modify the way hosts recognize and display your FxPlug plug-in.
- [Thread safety in plug-ins](./thread-safety-in-plug-ins.md)
  Learn about reentrancy for plug-ins and best practices to make them thread safe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/building-an-fxplug-plug-in-from-an-xcode-template)*