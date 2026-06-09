# Distribution

**Framework**: Technology Overviews

Distribute your apps on the App Store, or make them available to people directly from your website.

The App Store provides a safe and trusted way for people to find and install apps on all Apple platforms. When you distribute your app on the App Store, your apps can reach people in 175 countries and regions and in 40 languages. The App Store also helps you manage downloadable content like in-app purchases, subscriptions, and your company’s promotions.

If you’re creating apps for macOS, you can distribute apps outside the App Store and still offer people the safety and security they expect. Apple’s automated notarization workflow ensures that people receive your genuine app and that tampering didn’t occur during distribution.

#### Distribute Apps on the App Store

Make your apps available on the App Store with App Store Connect [`on the web`](https://developer.apple.comhttps://applestoreconnect.apple.com), on the app for [`iPhone and iPad`](https://developer.apple.comhttps://apps.apple.com/us/app/app-store-connect/id1234793120), or with the [`App Store Connect API`](https://developer.apple.com/documentation/AppStoreConnectAPI). Use App Store Connect to specify detailed information about your apps, and the legal and financial documents Apple needs to pay you for any sales. Specifically, use App Store Connect to:

- [`Add the apps`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/create-an-app-record/add-a-new-app) you want to sell, and [`add details`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/app-information) about those apps.
- Specify the [`price`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-app-pricing/set-a-price) of your app, and whether it supports [`in-app purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/overview-for-configuring-in-app-purchases) or any [`autorenewable`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/offer-auto-renewable-subscriptions) or [`nonrenewable`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-in-app-purchases/create-non-renewing-subscriptions) subscriptions.
- Invite people to [`test your apps and games`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview) with [`TestFlight`](https://developer.apple.comhttps://testflight.apple.com/).
- [`Submit your app`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-an-app) to the App Store for distribution.
- Monitor [`sales`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/view-sales-and-trends/view-units-proceeds-sales-and-pre-orders) and [`analytics`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/view-app-analytics/view-app-metrics) for your apps.
- Create [`In-App Events`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/offer-in-app-events/overview-of-in-app-events) and other [`promotions`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/offer-promo-codes/request-and-manage-promo-codes) to encourage people to download your app or use specific features.

Xcode and Xcode Cloud make it easy to distribute new builds of your software to App Store Connect. [`Preparing your app for distribution`](https://developer.apple.com/documentation/Xcode/preparing-your-app-for-distribution) for distribution by supplying the information App Store Connect needs. After you build a distributable version of your app, [`Distributing your app for beta testing and releases`](https://developer.apple.com/documentation/Xcode/distributing-your-app-for-beta-testing-and-releases) and send it to App Store Connect. If you use Xcode Cloud to build your app, [`Configuring your first Xcode Cloud workflow`](https://developer.apple.com/documentation/Xcode/Configuring-Your-First-Xcode-Cloud-Workflow) to upload your app after a successful build and distribute it to testers or the App Store.

#### Distribute Apps Yourself

In macOS, the Gatekeeper security technology ensures that only trusted software runs on a person’s Mac. When someone downloads and opens an app, plug-in, or installer package from outside the App Store, Gatekeeper verifies that the software is from a known developer and is unaltered. The first time someone runs the software on their Mac, Gatekeeper prompts them to verify they want to run the software.

If you distribute software outside the App Store, [`notarize it`](https://developer.apple.comdocumentation/security/notarizing-macos-software-before-distribution) so Gatekeeper can verify your software is genuine and unaltered. Notarization isn’t the same as an App Review. The Apple notary service is an automated system that scans your software for malicious content, checks for code-signing issues, and returns the results to you quickly. The system gives you a ticket to distribute with your software. When someone runs your software, Gatekeeper uses that ticket to verify your content is genuine and not altered. The notarization service also maintains an audit trail of software distributed using your signing key. If someone distributes an unauthorized version of your software, you can work with Apple to revoke the notarization of that version.

In eligible regions, you can [`Distributing your app from your website`](https://developer.apple.com/documentation/marketplacekit/distributing-your-app-from-your-website) for non-macOS platforms from your website or an [`Distributing your app on an alternative app marketplace`](https://developer.apple.com/documentation/marketplacekit/distributing-your-app-on-an-alternative-marketplace). In those regions, work with Apple to validate and notarize your content prior to distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/distribution)*