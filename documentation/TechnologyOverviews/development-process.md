# Development process

**Framework**: Technology Overviews

Discover the tools, programming languages, and resources you use to develop apps on Apple platforms.

Xcode is Apple’s integrated developer environment (IDE). It offers the tools you need to develop, test, and distribute apps for Apple platforms, including predictive code completion, generative intelligence powered by the best coding models and agents, advanced profiling and debugging tools, and simulators for Apple devices. Use it to create:

- [`App design and UI`](app-design-and-ui.md) that you ship on the App Store
- [`App and system extensions`](app-extensions.md) that augment system or app-specific features
- [`Swift packages`](https://developer.apple.com/documentation/xcode/swift-packages), libraries, and frameworks that contain code for distribution
- [`Automate tasks with shell scripts`](development-process#Automate-tasks-with-shell-scripts.md), [`Command-line tools`](https://developer.apple.com/documentation/xcode/command-line-tools), [`Writing documentation`](https://developer.apple.com/documentation/xcode/writing-documentation), and other types of content

Download the latest version of Xcode from the Mac App Store, or from the [`developer website`](https://developer.apple.comhttps://developer.apple.com/xcode/).

#### Get Started with the Swift Programming Language

[`Swift`](https://developer.apple.comhttps://www.swift.org/) is the best language for developing software on Apple platforms. It’s [`easy to get started`](https://developer.apple.comhttps://developer.apple.com/tutorials/develop-in-swift/), and modern features like built-in concurrency support, safe type handling, and automatic memory management deliver the safety and performance that production apps demand. If you’re starting a new project, Swift is a great choice for writing your code. Swift is also interoperable with [`Safely mix C, C++, and Swift`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/311), and [`Explore Swift and Java interoperability`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/307), making it easy to integrate Swift code into your existing codebase. The following type declaration shows the simplicity of Swift syntax.

```swift
// Type declaration and implementation.
struct PersonRecord {
    let name: String
    var age: Int = 0

    // Initialize a new instance of the type.
    init(_ name: String) {
        self.name = name
    }
    
    // Declare a function to update the age.
    func updateAge(_ newAge: Int) {
        guard let newAge > 0 else { return }
        age = newAge
    }
}
```

Xcode also supports [`Objective-C Runtime`](https://developer.apple.com/documentation/objectivec), a strict superset of the C programming language that adds object-oriented capabilities and a dynamic runtime. Many system frameworks provide Objective-C interfaces, so you can use their functionality in your existing Objective-C code bases to build apps and other types of software. You can include both Swift and Objective-C source files in the same project, along with code written in C, C++, Java, and other languages.

#### Manage Your Project Resources

Start any new project with Xcode, which you can [`download from the Mac App Store`](https://developer.apple.comhttps://apps.apple.com/us/app/xcode/id497799835?mt=12) or the [`developer website`](https://developer.apple.comhttps://developer.apple.com/xcode/). Create new projects and use the app to [`Projects and workspaces`](https://developer.apple.com/documentation/xcode/projects-and-workspaces), [`Asset management`](https://developer.apple.com/documentation/xcode/asset-management), [`Configuring the build settings of a target`](https://developer.apple.com/documentation/xcode/configuring-the-build-settings-of-a-target), and other project-related resources.

In an Xcode project, [`Build system`](https://developer.apple.com/documentation/xcode/build-system) tell Xcode what to build and how to build it. Each target specifies the list of files to compile and the build settings to use. Add scripts to your target to customize the build process or call your own tools. Add dependencies to your target to build products in a specific order. For example, you might build a library first, followed by the app that requires that library.

In Xcode, take advantage of several other key features:

- Write code, fix bugs, and and navigate unfamiliar code bases using [`Writing code with intelligence in Xcode`](https://developer.apple.com/documentation/xcode/writing-code-with-intelligence-in-xcode).
- Track and manage changes to your code using the integrated [`Source control management`](https://developer.apple.com/documentation/xcode/source-control-management).
- [`Adding previews to your interface files`](https://developer.apple.com/documentation/xcode/adding-previews-to-your-interface-files) as you build it.
- [`Running code snippets using the playground macro`](https://developer.apple.com/documentation/xcode/running-code-snippets-using-the-playground-macro) to verify it delivers the results you expect.
- Use [`Managing assets with asset catalogs`](https://developer.apple.com/documentation/xcode/managing-assets-with-asset-catalogs) to simplify the management of [`Adding images to your Xcode project`](https://developer.apple.com/documentation/xcode/adding-images-to-your-xcode-project), [`Specifying your app’s color scheme`](https://developer.apple.com/documentation/xcode/specifying-your-apps-color-scheme), and other project assets you ship with your code.
- Use [`Localizing and varying text with a string catalog`](https://developer.apple.com/documentation/xcode/localizing-and-varying-text-with-a-string-catalog) to manage string resources, including localized and customized versions of those strings.
- Create [`Creating managed asset packs`](https://developer.apple.com/documentation/backgroundassets/creating-managed-asset-packs) for assets that you ship separately from your app and [`Background Assets`](https://developer.apple.com/documentation/backgroundassets).
- Turn code comments into formatted documentation using [`Writing documentation`](https://developer.apple.com/documentation/xcode/writing-documentation).

You can also create some types of content with the additional apps that come with Xcode:

- Create your app’s icons using [`Icon Composer`](https://developer.apple.comhttps://developer.apple.com/icon-composer/).
- Explore the library of scalable images you can include in your app’s interface using [`SF Symbols`](https://developer.apple.comhttps://developer.apple.com/sf-symbols/).
- Create 3D objects and scenes using [`Reality Composer Pro`](https://developer.apple.com/documentation/realitycomposerpro), and animate the objects in your scenes with the help of [`RealityKit`](https://developer.apple.com/documentation/realitykit).
- Train machine learning models on your own data using [`Create ML`](https://developer.apple.com/documentation/createml).
- Display, query, and test accessibility information from your app’s UI using [`Accessibility Inspector`](https://developer.apple.com/documentation/accessibility/accessibility-inspector).

If you already have your own build tools and scripts, [`Installing the command-line tools`](https://developer.apple.com/documentation/xcode/installing-the-command-line-tools) the Xcode command-line tools so you can integrate its compilers and tools into your existing workflow.

#### Run and Debug Your Code

Xcode’s integrated [`Build system`](https://developer.apple.com/documentation/xcode/build-system) compiles your source files and assets into the final software product. This build system incorporates a wide range of tools, many of which you can also run from the [`Command-line tools`](https://developer.apple.com/documentation/xcode/command-line-tools). After a successful build, run the software on your Mac or install it on an actual device and debug it there.

During development, run your iOS, iPadOS, watchOS, tvOS, or visionOS app in [`Running your app on simulated or physical devices`](https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices) to quickly test your app’s behavior. Simulator runs on Mac, but simulates the runtime environment of iPhone, iPad, Apple TV, Apple Vision Pro, Apple Watch, and CarPlay. Use your Mac’s keyboard and mouse to simulate input like touch events, gestures, head movements, and other input. You can also simulate scenarios like location changes, memory warnings, network throttling, and more to verify your code behaves as expected.

To test your app’s CarPlay behavior, install your app on an iPhone, connect the iPhone to your Mac, and run the CarPlay Simulator app. This app simulates a variety of vehicle display configurations your app might encounter. The CarPlay Simulator app is part of the additional tools for Xcode that you [`download separately`](https://developer.apple.comhttps://developer.apple.com/download/all/?q=Xcode) from the Apple developer website.

#### Adopt Best Practices During Development

To reduce bugs and improve the performance of your code, it’s important to follow good practices during development. Testing your software regularly ensures that new code doesn’t introduce bugs or cause regressions. Similarly, collecting data regularly about your app’s performance helps you find issues early and fix them while there’s time to do so. Some other ways to improve the quality and performance of your code include:

- Start each new project or target from an [`Creating an Xcode project for an app`](https://developer.apple.com/documentation/xcode/creating-an-xcode-project-for-an-app), which configures the initial files and build settings you need.
- Store your projects in a [`Source control management`](https://developer.apple.com/documentation/xcode/source-control-management) (SCM) system. Whether you use `git` or another system, source management makes it easier for teams to collaborate on the same project. Configure this repository when you [`Configuring your Xcode project to use source control`](https://developer.apple.com/documentation/xcode/configuring-your-xcode-project-to-use-source-control) or at any time later.
- Define a clear branch strategy for projects in your repository and integrate changes using pull requests. A clear branch strategy helps developers navigate your repo and put changes in the correct place. Pull requests ensure changes receive proper review and are easier to revert if needed.
- Write [`Adding tests to your Xcode project`](https://developer.apple.com/documentation/xcode/adding-tests-to-your-xcode-project) for all new code. Require developers to run unit tests successfully on their local Mac before submitting any changes in a pull request.
- Use a continuous integration and delivery (CI/CD) system such as [`Xcode Cloud`](https://developer.apple.com/documentation/xcode/xcode-cloud), to run larger test suites automatically and to generate builds for your team.
- Collect [`Performance and metrics`](https://developer.apple.com/documentation/xcode/performance-and-metrics) for every pull request, and whenever you discover a performance regression. Take regular measurements to determine if performance is improving or regressing.

#### Automate Tasks with Shell Scripts

If your team already has dedicated scripts and tools for building your content, you can integrate Xcode tools into your scripts to build your software on Mac. The Xcode app contains the command-line tools you need, but you can also [`Installing the command-line tools`](https://developer.apple.com/documentation/xcode/installing-the-command-line-tools) to systems that don’t have Xcode. The set of [`Xcode command-line tool reference`](https://developer.apple.com/documentation/xcode/xcode-command-line-tool-reference) includes:

- `xcodebuild`, which interacts with Xcode projects and other features of the Xcode app.
- The `swift`, `clang`, and `llvm` tools, which provide the compiler frontends. Use them to build your Swift, C, C++, Objective-C, and Objective-C++ code.
- The `make` tool, which you use to run builds and create your software.
- The `linker` tool, which you use to link your intermediate build files together and create your final executable file.

And many more.

#### Get Information and Support

When you want the latest news and information about Apple development, look for it in the [`Developer`](https://developer.apple.comhttps://apps.apple.com/us/app/apple-developer/id640199958) app. Browse news, features, and developer stories originating in the wider community. You can watch Apple engineers explain how to use their technologies each year at Apple’s [`world-wide developer conference`](https://developer.apple.comhttps://developer.apple.com/wwdc) (WWDC), and catch up on videos from past conferences.

In addition to the Developer app, explore the [`Human Interface Guidelines`](https://developer.apple.com/design/human-interface-guidelines) and [`Apple developer documentation`](https://developer.apple.comhttps://developer.apple.com/documentation). The Human Interface Guidelines offer best practices and guidance for how to create a great experience. The developer documentation teaches you how to use the system frameworks, RESTful APIs, and other technologies through practical and useful sample code, articles, and API reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/development-process)*