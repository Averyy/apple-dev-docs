# Apps

**Framework**: App Store Connect API

Manage your apps in App Store Connect.

#### Overview

An `apps` resource represents your app that’s currently in development, or available on the App Store through the App Store Connect website. Use the `apps` resource to manage and maintain your existing apps.

Don’t use this API to create new apps; instead, create new apps on the App Store Connect website. To upload builds to App Store Connect, you must use Xcode, Transporter, or the Transporter Mac app. This API doesn’t permit you to directly upload your builds, but you may use App Store Connect API Keys in conjunction with Transporter to upload. To download the Transporter app, see the [`Mac App Store`](https://developer.apple.comhttps://apps.apple.com/us/app/transporter/id1450874784?mt=12).

To learn more about managing your apps, see [`Add a new app`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/create-an-app-record/add-a-new-app).

## Topics

### Getting and modifying app information
- [List Apps](get-v1-apps.md)
  Find and list apps in App Store Connect.
- [Read App Information](get-v1-apps-_id_.md)
  Get information about a specific app.
- [Modify an App](patch-v1-apps-_id_.md)
  Update app information, including bundle ID, primary locale, price schedule, and global availability.
- [Read an App’s Encryption Declarations](get-v1-apps-_id_-appencryptiondeclarations.md)
  Find and list all available app encryption declarations.
### Getting app build and prerelease version information
- [List All Builds of an App](get-v1-apps-_id_-builds.md)
  Get a list of builds associated with a specific app.
- [List All Prerelease Versions for an App](get-v1-apps-_id_-prereleaseversions.md)
  Get a list of prerelease versions associated with a specific app.
### Getting App Clip information
- [List All App Clips for an App](get-v1-apps-_id_-appclips.md)
  List your app’s associated App Clips.
### Getting beta tester information for TestFlight
- [List All Beta Groups for an App](get-v1-apps-_id_-betagroups.md)
  Get a list of beta groups associated with a specific app.
- [Remove Specified Beta Testers from All Groups and Builds of an App](delete-v1-apps-_id_-relationships-betatesters.md)
  Remove one or more beta testers’ access to test any builds of a specific app.
### Getting an app’s TestFlight details
- [Read the Beta App Review Details Resource of an App](get-v1-apps-_id_-betaappreviewdetail.md)
  Get the beta app review details for a specific app.
- [Read the Beta License Agreement of an App](get-v1-apps-_id_-betalicenseagreement.md)
  Get the beta license agreement for a specific app.
- [List All Beta App Localizations of an App](get-v1-apps-_id_-betaapplocalizations.md)
  Get a list of localized beta test information for a specific app.
### Getting an app’s Xcode Cloud products
- [Read the Xcode Cloud Product for an App](get-v1-apps-_id_-ciproduct.md)
  Get the Xcode Cloud product information for an app you build with Xcode Cloud.
### Getting an app’s price points
- [List all price points for an app](get-v1-apps-_id_-apppricepoints.md)
  Get all the available price points for a specific app.
- [Read app price point information](get-v3-apppricepoints-_id_.md)
  Get details about a specific app price point.
- [List app price point equalizations](get-v3-apppricepoints-_id_-equalizations.md)
  List all equivalent app prices points to a base price point.
### Getting App Store details for your app
- [List All App Infos for an App](get-v1-apps-_id_-appinfos.md)
  Get information about an app that is currently live on App Store, or that goes live with the next version.
- [List All App Store Versions for an App](get-v1-apps-_id_-appstoreversions.md)
  Get a list of all App Store versions of an app across all platforms.
- [Read the End User License Agreement Information of an App](get-v1-apps-_id_-enduserlicenseagreement.md)
  Get the custom end user license agreement (EULA) for a specific app and the territories where the agreement applies.
- [List all custom product pages for an app](get-v1-apps-_id_-appcustomproductpages.md)
  Get a list of all custom product pages for a specific app.
- [GET /v1/apps/{id}/appStoreVersionExperimentsV2](get-v1-apps-_id_-appstoreversionexperimentsv2.md)
### Getting in-app purchase information
- [Read In-App Purchase Information](get-v1-inapppurchases-_id_.md)
  Get information about an in-app purchase.
- [List All Promoted Purchases for an App](get-v1-apps-_id_-promotedpurchases.md)
  Get a list of promoted in-app purchases, including promoted auto-renewable subscriptions, for an app.
- [List All In-App Purchases for an App V1](get-v1-apps-_id_-inapppurchases.md)
  List the in-app purchases that are available for your app.
### Getting review submissions
- [Get review submissions for an app](get-v1-apps-_id_-reviewsubmissions.md)
  Get a list of review submissions associated with a specific app.
### Getting power and performance metrics
- [Get Power and Performance Metrics for an App](get-v1-apps-_id_-perfpowermetrics.md)
  Get the performance and power metrics data for the most recent version of an app.
### Getting customer reviews
- [List All Customer Reviews for an App](get-v1-apps-_id_-customerreviews.md)
  Get a list of customer reviews for a specific app.
### Getting and managing an app’s price schedules
- [Read price schedule information for an app](get-v1-apps-_id_-apppriceschedule.md)
  Read price schedule details for a specific app.
- [Read an app's price schedule information](get-v1-apppriceschedules-_id_.md)
  List the price schedule details for a specific app.
- [List automatically generated prices for an app](get-v1-apppriceschedules-_id_-automaticprices.md)
  List the automatically calculated prices for an app generated from a base territory.
- [Read the base territory for an app's price schedule](get-v1-apppriceschedules-_id_-baseterritory.md)
  Read the base territory and currency for a specific app.
- [List manually chosen prices for an app](get-v1-apppriceschedules-_id_-manualprices.md)
  List the prices you chose for a specific app.
- [Add a scheduled price change to an app](post-v1-apppriceschedules.md)
  Create a scheduled price change for an app.
### Getting and managing an app’s availability
- [List availability for an app](get-v1-apps-_id_-appavailabilityv2.md)
  Get a list of availabilities for a specific app.
### Getting beta tester metrics
- [Read beta tester metrics for an app](get-v1-apps-_id_-metrics-betatesterusages.md)
  Get usage metrics for beta testers of a specific app.
### Getting alternative distribution information
- [Read an app’s alternative distribution key](get-v1-apps-_id_-alternativedistributionkey.md)
  Get the alternative distribution keys for a specific app.
- [Read the marketplace search detail URL](get-v1-apps-_id_-marketplacesearchdetail.md)
  Get search detail URL for the alternative marketplace.
### Objects and data types
- [object App](app.md)
  The data structure that represents an Apps resource.
- [object AppWithoutIncludesResponse](appwithoutincludesresponse.md)
- [object AppsWithoutIncludesResponse](appswithoutincludesresponse.md)
- [object AppUpdateRequest](appupdaterequest.md)
  The request body you use to update an App Update.
- [object AppClipsResponse](appclipsresponse.md)
  A response that contains a list of App Clips resources.
- [object AppResponse](appresponse.md)
  A response that contains a single Apps resource.
- [object AppsResponse](appsresponse.md)
  A response that contains a list of Apps resources.
- [object InAppPurchase](inapppurchase.md)
  The data structure that represents the In-App Purchases resource.
- [object InAppPurchaseResponse](inapppurchaseresponse.md)
  A response that contains a single In-App Purchases resource.
- [object InAppPurchasesResponse](inapppurchasesresponse.md)
  A response that contains a list of In-App Purchases resources.
- [object AppBetaTestersLinkagesRequest](appbetatesterslinkagesrequest.md)
  A request body you use to remove beta testers from an app.
- [object AppPricePointV3](apppricepointv3.md)
  The data structure that represents an App Price Point V3 resource.
- [object AppPricePointV3Response](apppricepointv3response.md)
- [object AppPricePointsV3Response](apppricepointsv3response.md)
- [object AppPriceSchedule](apppriceschedule.md)
- [object AppPriceScheduleCreateRequest](apppriceschedulecreaterequest.md)
- [object AppPriceScheduleResponse](apppricescheduleresponse.md)
- [object AppPriceV2](apppricev2.md)
- [object AppPriceV2InlineCreate](apppricev2inlinecreate.md)
  The data structure that represents a App Price V2 Inline Create resource.
- [object AppPricesV2Response](apppricesv2response.md)
- [object TerritoryInlineCreate](territoryinlinecreate.md)
- [type Platform](platform.md)
  Strings that represent Apple operating systems.
- [type SubscriptionStatusUrlVersion](subscriptionstatusurlversion.md)
  Strings that represent versions of App Store Server Notifications.
- [object App.Relationships.InAppPurchases](app/relationships-data.dictionary/inapppurchases-data.dictionary.md)
  The data and links that describe the relationship between the resources.

## See Also

- [App Metadata](app-metadata.md)
  Manage the metadata of apps in App Store Connect.
- [Custom Product Pages and Localizations](custom-product-pages-and-localizations.md)
  Create and manage your app’s custom product pages and localizations.
- [App Events and Metadata](app-events-and-metadata.md)
  Create and schedule in-app events and manage in-app event metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/apps)*