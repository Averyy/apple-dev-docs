# Testing and performance

**Framework**: Technology Overviews

Discover and fix potential issues in your code by testing and regularly collecting performance metrics.

Testing your code and analyzing its performance throughout the development process can take your project to the next level. A comprehensive set of tests helps you verify your code runs the way you expect, and performance metrics help you determine if your app uses resources efficiently. When you regularly gather test and performance data, you become aware of problems early, and have time to fix them.

#### Create a test plan for your project

A [test plan](../Xcode/organizing-tests-to-improve-feedback.md) is an essential part of the development process for teams of all sizes. A test plan comprises several elements:

- [Unit tests](./testing-and-performance.md#Write-unit-tests-for-your-code) that validate individual behaviors of a type or feature.
- [UI tests](./testing-and-performance.md#Test-interactions-with-your-apps-interface) that validate how your app responds to direct interactions with its interface.
- Test suites, or groups of tests, that you run together to validate a particular type or feature.
- Test bundles, or collections of test suites, that you run to validate your entire codebase.

In Xcode, [add a test bundle](../Xcode/adding-tests-to-your-xcode-project.md) to your project and use it to create your initial tests and test suites. Each test bundle has an associated target that you build and run before you run the tests. You can run your tests every time you build a target, or run them only at specific times. For example, you might run tests only before you submit changes to your source control system.

The Test navigator pane in your Xcode project displays the overall test plan for your project, and the tests from all your test bundles. [Run your test plan](../Xcode/running-tests-and-interpreting-results.md) from Xcode or the command line, and verify the results before submitting any code changes to the project. Automate your tests by running your test plan in [Xcode Cloud](../Xcode/xcode-cloud.md).

#### Write unit tests for your code

A unit test is a function that runs some of your code and determines whether that code delivered the expected results. You can create any number of unit tests for your app and use them to validate the behavior of specific types or features. For example, one test might verify that a custom object adds data correctly, while a second test verifies the removal process.

To write unit tests for your code, [add a test bundle](../Xcode/adding-tests-to-your-xcode-project.md) to your project and configure it to use the [Swift Testing](../Testing/Testing.md) or [XCTest](../XCTest/XCTest.md) framework. Both frameworks provide code-level support for writing unit test functions and checking the expected results. [Swift Testing](../Testing/Testing.md) provides powerful and expressive tools to declare and manage your unit tests, and it’s a great choice for testing your Swift code. Use [XCTest](../XCTest/XCTest.md) for any UI tests you create, and for code you write using Swift, Objective-C, and other C-based languages. To test your app’s In-App Purchase code, include the [StoreKit Test](../StoreKitTest/StoreKitTest.md) framework in addition to one of the other frameworks.

The following listing shows the same unit test in [Swift Testing](../Testing/Testing.md) and [XCTest](../XCTest/XCTest.md). Swift Testing uses a macro-based approach to [mark up test functions](../Testing/definingtests.md), leading to short and easy-to-read test code. Create dedicated XCTest types and use them to [define your test cases](../XCTest/defining-test-cases-and-test-methods.md).

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

#### Test interactions with your app’s interface

UI tests verify that the code for your app’s interface delivers expected results. The tests simulate direct interactions with your app’s interface, and capture the results for you to examine. Like unit tests, you use UI tests to test specific workflows in your app. For example, a test might open a data entry form, populate the fields with specific values, and verify your code handles the data correctly.

Create UI tests inside [a UI Testing Bundle](../Xcode/adding-tests-to-your-xcode-project.md) and write them using [XCTest](../XCTest/XCTest.md) and the [XCUIAutomation](../XCUIAutomation/XCUIAutomation.md) framework. XCTest provides the types you use to create your tests, and XCUIAutomation works with your app’s [accessibility support](../Accessibility/Accessibility.md) to give you references to views and other elements in your interface.

Xcode offers a way to [record interactions with your app](../XCUIAutomation/recording-ui-automation-for-testing.md), and turn them into the code for a UI test function. After you record a set of interactions, augment the generated code to check values or the state of your app. Rewrite the transcribed UI interactions as needed to make your tests more robust.

In your test plan, run your UI tests on a variety of devices and languages your app supports. Different configurations help you identify problems you might not have anticipated. For example, testing on different devices show you places where your UI doesn’t adjust properly. Similarly, testing in different languages can uncover [internationalization](../Xcode/localization.md) issues.

#### Adopt a continuous integration and delivery strategy

To catch errors as early as possible, run tests regularly and analyze the results. [Xcode Cloud](../Xcode/about-continuous-integration-and-delivery-with-xcode-cloud.md) is a continuous integration and delivery (CI/CD) system that integrates with Xcode, TestFlight, and App Store Connect. Use it to [create workflows](https://developer.apple.com/videos/play/wwdc2023/10278) that build your project and run tests automatically in iCloud. For example, a workflow might build and run your tests each time a developer merges a pull request. You can specify different devices and languages to use during testing, and you can even run custom scripts to handle project-specific actions.

For UI tests, you can configure Xcode Cloud to capture videos of each test as it runs. If a particular test fails, use these videos as a first step to diagnose the failure. Use the other information that Xcode Cloud collects to inspect your UI and locate where a particular test failed.

#### Gather and analyze performance metrics

Efficiency is about maximizing the amount of work your app performs while minimizing its use of memory, battery, and other system resources. Improving your code’s efficiency can help it run faster, use less memory, and use less energy. These adjustments help improve the overall experience people have with your app.

Instruments [captures real-time insights](../Xcode/improving-your-app-s-performance.md) about what your code is doing and what resources it’s using. After you collect a set of baseline performance metrics, capture new sets periodically to determine if performance improved or diminished. Use Instruments to collect data about:

- The time it takes your app to [launch](../Xcode/reducing-your-app-s-launch-time.md).
- The amount of [memory your app uses](../Xcode/reducing-your-app-s-memory-use.md), and how it uses that memory.
- How often [SwiftUI views](../Xcode/understanding-and-improving-swiftui-performance.md) update their contents.
- Places where your code [stalls the CPU](../Xcode/addressing-cpu-bottlenecks.md) or runs code inefficiently.
- How much time your app spends [blocked](../Xcode/improving-app-responsiveness.md) waiting for files, threads, network data, or other resources.
- Where your app’s graphics code experiences [hitches](../Xcode/understanding-hitches-in-your-app.md) or [hangs](../Xcode/understanding-hangs-in-your-app.md).
- How much [energy your app consumes](../Xcode/reducing-your-app-s-battery-use.md) when it runs.
- The efficiency of your app’s concurrent tasks.

You can run Instruments with the same tests you create to validate your app’s behavior, or you can build custom tests to collect performance metrics for specific features. Sample your code to identify potential problems, and switch to a [processor trace](../Xcode/analyzing-cpu-usage-with-processor-trace.md) as needed to see the precise set of branches your code takes when running in the CPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/testing-and-performance)*