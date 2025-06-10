# Getting started with ThreadNetwork

**Framework**: ThreadNetwork

Create a plan to build, test, and deploy your Thread Border Router app.

#### Overview

Creating a Thread Border Router enabled app or device requires configuring your app’s Xcode project to enable testing the ThreadNetwork API capabilities. Perform these in a specific order to ensure your app meets requirements for submission to the App Store. The development process follows these basic steps:

1. Xcode provides a Manage Thread Network Credentials capability for use while your app is under development.
2. Once your app is feature complete, ensure that its operation and specifications conform to the Thread device test plan.
3. Before submitting your app for approval and sale on the App Store, apply for a Thread Network distribution entitlement.
4. Optionally, apply to use the  badge to alert people to your app’s ability to work with Apple Home.

#### Create and Configure Your Xcode Project for Development

Create a new Xcode project for your app and apply the following settings to your new project:

1. Add the Managed Network Credentials (development) capability to your project — select your app’s target in the project navigator, click on capabilities, and search for “Manage Thread Network Credentials.” Double-click on the resulting entitlement to add it to your app’s entitlements.
2. In your app, add `import ThreadNetwork` to import the Thread framework support.
3. Add Thread Border Router configuration and management capabilities to your app; for information on router configuration, see [`Configuring a Border Router`](configuring-a-border-router.md). For information on managing credentials, see [`com.apple.developer.networking.manage-thread-network-credentials`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.networking.manage-thread-network-credentials).

#### Perform Required Conformance Testing

Ensure your app is ready for submission by completing these tests:

1. Implement the test plans for User Experience and Thread Clients. For information on the required User Experience testing, see [`Thread Test Plan User Experience`](https://developer.apple.comhttps://developer.apple.com/apple-home/downloads/Thread-Test-Plan-User-Experience-R1.pdf). For information on the required Thread Client testing, see [`Thread Test Plan THClient API`](https://developer.apple.comhttps://developer.apple.com/apple-home/downloads/Thread-Test-Plan-THClient-API-R1.pdf).
2. After your app passes the required tests you need to submit the test results to Apple to apply for a distribution entitlement. For a sample spreadsheet and checklist that lists all test sections and components, see [`ThreadNetwork Test Result Checklist`](https://developer.apple.comhttps://developer.apple.com/apple-home/downloads/ThreadNetwork-Test-Result-Checklist.zip). To submit your results for validation, send them to [`tthreadsoftware@apple.com`](https://developer.apple.commailto:tthreadsoftware@apple.com).

> **Note**: If you’re developing an accessory that implements Apple HomeKit technology, you need to be a member of the MFi Program. For more information, see [`MFi Program`](https://developer.apple.comhttps://mfi.apple.com/) for any additional requirements that Apple HomeKit technology requires.

If you have questions about implementation issues or questions about API and tools, please submit a [`support request`](https://developer.apple.comhttps://developer.apple.com/support/technical/).

#### Prepare Your App for Approval and Distribution

After you receive confirmation of the approval of your app’s conformance test results, you can apply for  a distribution entitlement for your app. Request a distribution entitlement from the [`ThreadNetwork Framework Entitlement Request`](https://developer.apple.comhttps://developer.apple.com/contact/request/threadnetwork) page.

After Apple grants the distribution entitlement, go to the [`Developer Portal`](https://developer.apple.comhttps://developer.apple.com/account/) and enable the assigned Manage Thread Network Credentials entitlement for your app. You can then submit your app to the App Store.

After you begin shipping your device, you need to send a sample of your Thread Border Router device for verification to the following address:

NPI Certification 
1 Apple Park Way 
Mailstop 928-3WTE 
Cupertino, CA, 95014 
United States

#### Apply for the Works with Apple Home Badge

Optionally, you can also request the  badge for your Thread Border Router. This badge assures customers that your product works well with Apple Home.

To request permission to use the badge on your product and in marketing materials, follow these steps:

1. Become a member of the MFi Program; see MFi program note, above.
2. Become a member of the [`Thread Group`](https://developer.apple.comhttps://www.threadgroup.org), if you’re not already.
3. Complete the [`Thread Group certification`](https://developer.apple.comhttps://www.threadgroup.org/What-is-Thread/Certification) for your Thread border router.
4. Implement an app for the hardware that uses the ThreadNetwork framework, as described above.
5. Pass the required Apple Home Thread Border Router conformance tests, as described above.
6. Submit the completed test results to tthreadsoftware@apple.com for review.

## See Also

- [Configuring a Border Router](configuring-a-border-router.md)
  Set up or add a Border Router on a Thread network.
- [Managing Thread network credentials](managing-thread-network-credentials.md)
  Store, retrieve, update, and delete Thread network credentials on your Apple device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/getting-started-with-threadnetwork)*