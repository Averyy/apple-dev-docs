# Testing and performance

**Framework**: Technology Overviews

Discover and fix potential issues in your code by testing and regularly collecting performance metrics.

Testing your code and analyzing its performance throughout the development process can take your project to the next level. A comprehensive set of tests helps you verify your code runs the way you expect, and performance metrics help you determine if your app uses resources efficiently. When you regularly gather test and performance data, you become aware of problems early, and have time to fix them.

#### Create a Test Plan for Your Project

A [`Improving code assessment by organizing tests into test plans`](https://developer.apple.com/documentation/Xcode/organizing-tests-to-improve-feedback) is an essential part of the development process for teams of all sizes. A test plan comprises several elements:

- [`Write unit tests for your code`](testing-and-performance#Write-unit-tests-for-your-code.md) that validate individual behaviors of a type or feature.
- [`Test interactions with your app’s interface`](testing-and-performance#Test-interactions-with-your-apps-interface.md) that validate how your app responds to direct interactions with its interface.
- Test suites, or groups of tests, that you run together to validate a particular type or feature.
- Test bundles, or collections of test suites, that you run to validate your entire codebase.

In Xcode, [`Adding tests to your Xcode project`](https://developer.apple.com/documentation/Xcode/adding-tests-to-your-xcode-project) to your project and use it to create your initial tests and test suites. Each test bundle has an associated target that you build and run before you run the tests. You can run your tests every time you build a target, or run them only at specific times. For example, you might run tests only before you submit changes to your source control system.

The Test navigator pane in your Xcode project displays the overall test plan for your project, and the tests from all your test bundles. [`Running tests and interpreting results`](https://developer.apple.com/documentation/Xcode/running-tests-and-interpreting-results) from Xcode or the command line, and verify the results before submitting any code changes to the project. Automate your tests by running your test plan in [`Xcode Cloud`](https://developer.apple.com/documentation/Xcode/Xcode-Cloud).

#### Write Unit Tests for Your Code

A unit test is a function that runs some of your code and determines whether that code delivered the expected results. You can create any number of unit tests for your app and use them to validate the behavior of specific types or features. For example, one test might verify that a custom object adds data correctly, while a second test verifies the removal process.

To write unit tests for your code, [`Adding tests to your Xcode project`](https://developer.apple.com/documentation/Xcode/adding-tests-to-your-xcode-project) to your project and configure it to use the [`Swift Testing`](https://developer.apple.com/documentation/Testing) or [`XCTest`](https://developer.apple.com/documentation/XCTest) framework. Both frameworks provide code-level support for writing unit test functions and checking the expected results. [`Swift Testing`](https://developer.apple.com/documentation/Testing) provides powerful and expressive tools to declare and manage your unit tests, and it’s a great choice for testing your Swift code. Use [`XCTest`](https://developer.apple.com/documentation/XCTest) for any UI tests you create, and for code you write using Swift, Objective-C, and other C-based languages. To test your app’s In-App Purchase code, include the [`StoreKit Test`](https://developer.apple.com/documentation/StoreKitTest) framework in addition to one of the other frameworks.

The following listing shows the same unit test in [`Swift Testing`](https://developer.apple.com/documentation/Testing) and [`XCTest`](https://developer.apple.com/documentation/XCTest). Swift Testing uses a macro-based approach to [`Defining test functions`](https://developer.apple.com/documentation/Testing/DefiningTests), leading to short and easy-to-read test code. Create dedicated XCTest types and use them to [`Defining Test Cases and Test Methods`](https://developer.apple.com/documentation/XCTest/defining-test-cases-and-test-methods).

**Swift Testing**:

```swift
@Test func checkNewEmptyTable() {
    let table = Table()
    #expect(table.rowCount == 0)
    #expect(table.ColumnCount == 0)
}
```

**XCTest**:

```swift
class TableValidationTests: XCTestCase {
    /// Tests that a new table instance has zero rows and columns.
    func testEmptyTableRowAndColumnCount() {
        let table = Table()
        XCTAssertEqual(table.rowCount, 0, "Row count was not zero.")
        XCTAssertEqual(table.columnCount, 0, "Column count was not zero.")
    }
}
```

View your project’s unit tests in the Test navigator pane of the Xcode project window. Use this pane to run individual unit tests or groups of unit tests at any time. Alternatively, run tests directly from the source window that contains your test code. To collect performance metrics for your tests, run them in Instruments.

When deciding what tests to create, include a mixture of tests with both positive and negative outcomes. It’s important to verify your code handles data correctly, but it’s also important to verify your app handles boundary conditions or bad data correctly. For example, you might deliberately run a test with bad data to verify your code returns an appropriate error.

#### Test Interactions with Your Apps Interface

UI tests verify that the code for your app’s interface delivers expected results. The tests simulate direct interactions with your app’s interface, and capture the results for you to examine. Like unit tests, you use UI tests to test specific workflows in your app. For example, a test might open a data entry form, populate the fields with specific values, and verify your code handles the data correctly.

Create UI tests inside [`Adding tests to your Xcode project`](https://developer.apple.com/documentation/Xcode/adding-tests-to-your-xcode-project) and write them using [`XCTest`](https://developer.apple.com/documentation/XCTest) and the [`XCUIAutomation`](https://developer.apple.com/documentation/XCUIAutomation) framework. XCTest provides the types you use to create your tests, and XCUIAutomation works with your app’s [`Accessibility`](https://developer.apple.com/documentation/Accessibility) to give you references to views and other elements in your interface.

Xcode offers a way to [`Recording UI automation for testing`](https://developer.apple.com/documentation/XCUIAutomation/recording-ui-automation-for-testing), and turn them into the code for a UI test function. After you record a set of interactions, augment the generated code to check values or the state of your app. Rewrite the transcribed UI interactions as needed to make your tests more robust.

In your test plan, run your UI tests on a variety of devices and languages your app supports. Different configurations help you identify problems you might not have anticipated. For example, testing on different devices show you places where your UI doesn’t adjust properly. Similarly, testing in different languages can uncover [`Localization`](https://developer.apple.com/documentation/Xcode/localization) issues.

#### Adopt a Continuous Integration and Delivery Strategy

To catch errors as early as possible, run tests regularly and analyze the results. [`About continuous integration and delivery with Xcode Cloud`](https://developer.apple.com/documentation/Xcode/About-Continuous-Integration-and-Delivery-with-Xcode-Cloud) is a continuous integration and delivery (CI/CD) system that integrates with Xcode, TestFlight, and App Store Connect. Use it to [`Create practical workflows in Xcode Cloud`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10278) that build your project and run tests automatically in iCloud. For example, a workflow might build and run your tests each time a developer merges a pull request. You can specify different devices and languages to use during testing, and you can even run custom scripts to handle project-specific actions.

For UI tests, you can configure Xcode Cloud to capture videos of each test as it runs. If a particular test fails, use these videos as a first step to diagnose the failure. Use the other information that Xcode Cloud collects to inspect your UI and locate where a particular test failed.

#### Gather and Analyze Performance Metrics

Efficiency is about maximizing the amount of work your app performs while minimizing its use of memory, battery, and other system resources. Improving your code’s efficiency can help it run faster, use less memory, and use less energy. These adjustments help improve the overall experience people have with your app.

Instruments [`Improving your app’s performance`](https://developer.apple.com/documentation/Xcode/improving-your-app-s-performance) about what your code is doing and what resources it’s using. After you collect a set of baseline performance metrics, capture new sets periodically to determine if performance improved or diminished. Use Instruments to collect data about:

- The time it takes your app to [`Reducing your app’s launch time`](https://developer.apple.com/documentation/Xcode/reducing-your-app-s-launch-time).
- The amount of [`Reducing your app’s memory use`](https://developer.apple.com/documentation/Xcode/reducing-your-app-s-memory-use), and how it uses that memory.
- How often [`Understanding and improving SwiftUI performance`](https://developer.apple.com/documentation/Xcode/understanding-and-improving-swiftui-performance) update their contents.
- Places where your code [`Addressing CPU bottlenecks`](https://developer.apple.com/documentation/Xcode/addressing-cpu-bottlenecks) or runs code inefficiently.
- How much time your app spends [`Improving app responsiveness`](https://developer.apple.com/documentation/Xcode/improving-app-responsiveness) waiting for files, threads, network data, or other resources.
- Where your app’s graphics code experiences [`Understanding hitches in your app`](https://developer.apple.com/documentation/Xcode/understanding-hitches-in-your-app) or [`Understanding hangs in your app`](https://developer.apple.com/documentation/Xcode/understanding-hangs-in-your-app).
- How much [`Reducing your app’s battery use`](https://developer.apple.com/documentation/Xcode/reducing-your-app-s-battery-use) when it runs.
- The efficiency of your app’s concurrent tasks.

You can run Instruments with the same tests you create to validate your app’s behavior, or you can build custom tests to collect performance metrics for specific features. Sample your code to identify potential problems, and switch to a [`Analyzing CPU usage with the Processor Trace instrument`](https://developer.apple.com/documentation/Xcode/analyzing-cpu-usage-with-processor-trace) as needed to see the precise set of branches your code takes when running in the CPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/testing-and-performance)*