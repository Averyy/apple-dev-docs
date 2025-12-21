# Implementing a background delivery extension

**Framework**: FinanceKit

Receive up-to-date financial data in your app and its extensions by adding a background delivery extension.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Xcode 26.0+

#### Overview

This sample code project shows you how to create a background delivery extension with [`FinanceKit`](FinanceKit.md). With the extension, you can receive notifications when data changes in [`FinanceStore`](FinanceStore.md) and handle it outside of your app’s life cycle. This enables your app and its extensions to access up-to-date information without relying on the app itself.

> **Note**: This sample code project is associated with WWDC25 session 201: [`What’s new in Apple Pay`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/201).

##### Configure the Sample Code Project

To run the sample app, you need an entitlement from Apple, and to complete the following:

Add an extension target to your new or existing Xcode project. Choose File > New > Target and, in the sheet that appears, choose the `Background Delivery Extension` template under Application Extension, and click Next. Then fill out your options for your new target and click Finish. In the next dialog that appears click Activate to use the extension scheme Xcode creates. If you don’t have an Xcode project for your app, first create one from an Application template under iOS. For more information, see [`Creating an Xcode project for an app`](https://developer.apple.com/documentation/Xcode/creating-an-xcode-project-for-an-app).

Add the App Groups capability to both your app and extension target. For more information, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app). Then, add both targets to the same app group. In the project editor, select the app target, and then add a unique ID for the group under App Groups on the Signing & Capabilities pane. Xcode automatically selects the new group ID. Select the extension target, then go to App Groups, click Refresh, and select the same group ID. The app and extension are now in the same app group and can have access to the same shared data. For more information on configuring app groups, see [`Configuring app groups`](https://developer.apple.com/documentation/Xcode/configuring-app-groups).

To access someone’s financial data, you must meet the criteria outlined in [`Get started with FinanceKit`](https://developer.apple.comhttps://developer.apple.com/financekit/), request the [`FinanceKit managed entitlement`](https://developer.apple.comhttps://developer.apple.com/contact/request/financekit/), hold an organization-level Apple Developer account, be logged in as Account Holder, and include the `NSFinancialDataUsageDescription` string in your `Info.plist`.

Apple reviews each application using defined criteria. If your request meets the criteria, Apple adds the entitlement to your developer account by using managed capabilities. To request access, see the [`FinanceKit managed entitlement`](https://developer.apple.comhttps://developer.apple.com/contact/request/financekit/). For more information about managed entitlements, see [`Provisioning with capabilities`](https://developer.apple.comhttps://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities).

## See Also

- [FinanceKit updates](../Updates/FinanceKit.md)
  Learn more about changes to FinanceKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/implementing-a-background-delivery-extension)*