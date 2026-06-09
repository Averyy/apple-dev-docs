# Apps

**Framework**: App Store Connect API

Manage your apps in App Store Connect.

#### Overview

An `apps` resource represents your app that’s currently in development, or available on the App Store through the App Store Connect website. Use the `apps` resource to manage and maintain your existing apps.

Don’t use this API to create new apps; instead, create new apps on the App Store Connect website. To upload builds to App Store Connect, you must use Xcode, Transporter, or the Transporter Mac app. This API doesn’t permit you to directly upload your builds, but you may use App Store Connect API Keys in conjunction with Transporter to upload. To download the Transporter app, see the [`Mac App Store`](https://developer.apple.comhttps://apps.apple.com/us/app/transporter/id1450874784?mt=12).

To learn more about managing your apps, see [`Add a new app`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/create-an-app-record/add-a-new-app).

## Topics

### Getting and modifying app information
- [List apps](get-v1-apps.md)
  Find and list apps in App Store Connect.
- [Read app information](get-v1-apps-_id_.md)
  Get information about a specific app.
- [Modify an app](patch-v1-apps-_id_.md)
  Update app information, including bundle ID, primary locale, price schedule, and global availability.
- [Read an app’s encryption declarations](get-v1-apps-_id_-appencryptiondeclarations.md)
  Find and list all available app encryption declarations.
- [Read an app’s encryption declaration ids](get-v1-apps-_id_-relationships-appencryptiondeclarations.md)
  Find and list all available app encryption declaration IDs for a specific app.
### Getting app build and prerelease version information
- [List all builds of an app](get-v1-apps-_id_-builds.md)
  Get a list of builds associated with a specific app.
- [List build IDs for an app](get-v1-apps-_id_-relationships-builds.md)
- [List all prerelease versions for an app](get-v1-apps-_id_-prereleaseversions.md)
  Get a list of prerelease versions associated with a specific app.
- [List prerelease version IDs for an app](get-v1-apps-_id_-relationships-prereleaseversions.md)
### Getting App Clip information
- [List all app clips for an app](get-v1-apps-_id_-appclips.md)
  List your app’s associated App Clips.
- [List App Clip IDs for an app](get-v1-apps-_id_-relationships-appclips.md)
### Getting beta tester information for TestFlight
- [List all beta groups for an app](get-v1-apps-_id_-betagroups.md)
  Get a list of beta groups associated with a specific app.
- [List beta group IDs for an app](get-v1-apps-_id_-relationships-betagroups.md)
- [Remove specified beta testers from all groups and builds of an app](delete-v1-apps-_id_-relationships-betatesters.md)
  Remove one or more beta testers’ access to test any builds of a specific app.
### Getting an app’s TestFlight details
- [Read the beta app review details resource of an app](get-v1-apps-_id_-betaappreviewdetail.md)
  Get the beta app review details for a specific app.
- [Get the beta app review detail ID for an app](get-v1-apps-_id_-relationships-betaappreviewdetail.md)
- [Get the beta app review detail ID for an app](get-v1-apps-_id_-relationships-betaappreviewdetail.md)
- [Read the beta license agreement of an app](get-v1-apps-_id_-betalicenseagreement.md)
  Get the beta license agreement for a specific app.
- [Get the beta license agreement ID for an app](get-v1-apps-_id_-relationships-betalicenseagreement.md)
- [List all beta app localizations of an app](get-v1-apps-_id_-betaapplocalizations.md)
  Get a list of localized beta test information for a specific app.
- [List beta app localization IDs for an app](get-v1-apps-_id_-relationships-betaapplocalizations.md)
### Getting an app’s Xcode Cloud products
- [Read the xcode cloud product for an app](get-v1-apps-_id_-ciproduct.md)
  Get the Xcode Cloud product information for an app you build with Xcode Cloud.
- [Get the CI product ID for an app](get-v1-apps-_id_-relationships-ciproduct.md)
### Getting an app’s price points
- [List All Price Points for an App](get-v1-apps-_id_-apppricepoints.md)
  Get all the available price points for a specific app.
- [List app price point IDs for an app](get-v1-apps-_id_-relationships-apppricepoints.md)
- [Read App Price Point Information](get-v3-apppricepoints-_id_.md)
  Get details about a specific app price point.
- [List App Price Point Equalizations](get-v3-apppricepoints-_id_-equalizations.md)
  List all equivalent app prices points to a base price point.
- [List equalization price point IDs for an app price point](get-v3-apppricepoints-_id_-relationships-equalizations.md)
  Get a list of equalization price point IDs for a specific app price point.
### Getting App Store details for your app
- [List all app infos for an app](get-v1-apps-_id_-appinfos.md)
  Get information about an app that is currently live on App Store, or that goes live with the next version.
- [List app info IDs for an app](get-v1-apps-_id_-relationships-appinfos.md)
- [List all app store versions for an app](get-v1-apps-_id_-appstoreversions.md)
  Get a list of all App Store versions of an app across all platforms.
- [List App Store version IDs for an app](get-v1-apps-_id_-relationships-appstoreversions.md)
- [Read the end user license agreement information of an app](get-v1-apps-_id_-enduserlicenseagreement.md)
  Get the custom end user license agreement (EULA) for a specific app and the territories where the agreement applies.
- [Get the end user license agreement ID for an app](get-v1-apps-_id_-relationships-enduserlicenseagreement.md)
- [List All Custom Product Pages for an App](get-v1-apps-_id_-appcustomproductpages.md)
  Get a list of all custom product pages for a specific app.
- [Get all custom product page resource ids for an app](get-v1-apps-_id_-relationships-appcustomproductpages.md)
  Get a list of custom product page resource IDs associated with an app.
- [List all app store experiments for an app](get-v1-apps-_id_-appstoreversionexperimentsv2.md)
  Get a list of all App Store version experiments for a specific app.
- [List App Store version experiment IDs for an app](get-v1-apps-_id_-relationships-appstoreversionexperimentsv2.md)
### Getting in-app purchase information
- [Read in-app purchase information](get-v1-inapppurchases-_id_.md)
  Get information about an in-app purchase.
- [List all promoted purchases for an app](get-v1-apps-_id_-promotedpurchases.md)
  Get a list of promoted in-app purchases, including promoted auto-renewable subscriptions, for an app.
- [List all in-app purchases for an app v1](get-v1-apps-_id_-inapppurchases.md)
  List the in-app purchases that are available for your app.
### Getting review submissions
- [Get Review Submissions for an App](get-v1-apps-_id_-reviewsubmissions.md)
  Get a list of review submissions associated with a specific app.
- [List review submission IDs](get-v1-apps-_id_-relationships-reviewsubmissions.md)
  Get the list of review submission IDs for a specific app.
### Getting power and performance metrics
- [Get power and performance metrics for an app](get-v1-apps-_id_-perfpowermetrics.md)
  Get the performance and power metrics data for the most recent version of an app.
### Getting customer reviews
- [List all customer reviews for an app](get-v1-apps-_id_-customerreviews.md)
  Get a list of customer reviews for a specific app.
- [List customer review IDs for an app](get-v1-apps-_id_-relationships-customerreviews.md)
- [Read Customer Review Summarizations](get-v1-apps-_id_-customerreviewsummarizations.md)
  Get the customer review summarization for a specific app.
### Getting and managing an app’s price schedules
- [Read Price Schedule Information for an App](get-v1-apps-_id_-apppriceschedule.md)
  Read price schedule details for a specific app.
- [Get the app price schedule ID for an app](get-v1-apps-_id_-relationships-apppriceschedule.md)
- [Read an App's Price Schedule Information](get-v1-apppriceschedules-_id_.md)
  List the price schedule details for a specific app.
- [List Automatically Generated Prices for an App](get-v1-apppriceschedules-_id_-automaticprices.md)
  List the automatically calculated prices for an app generated from a base territory.
- [Read the Base Territory for an App's Price Schedule](get-v1-apppriceschedules-_id_-baseterritory.md)
  Read the base territory and currency for a specific app.
- [List Manually Chosen Prices for an App](get-v1-apppriceschedules-_id_-manualprices.md)
  List the prices you chose for a specific app.
- [List automatic price IDs for an app price schedule](get-v1-apppriceschedules-_id_-relationships-automaticprices.md)
- [Get the base territory ID for an app price schedule](get-v1-apppriceschedules-_id_-relationships-baseterritory.md)
- [List manual price IDs for an app price schedule](get-v1-apppriceschedules-_id_-relationships-manualprices.md)
- [Add a Scheduled Price Change to an App](post-v1-apppriceschedules.md)
  Create a scheduled price change for an app.
### Getting and managing an app’s availability
- [List Availability for an App](get-v1-apps-_id_-appavailabilityv2.md)
  The data structure that represents a get-v1-apps-{id}-app availability v2 resource.
- [Get the app availability ID for an app](get-v1-apps-_id_-relationships-appavailabilityv2.md)
### Getting beta tester metrics
- [Read Beta Tester Metrics for an App](get-v1-apps-_id_-metrics-betatesterusages.md)
  Get usage metrics for beta testers of a specific app.
### Getting app event information
- [List all in-app events for an app](get-v1-apps-_id_-appevents.md)
  Get a list of in-app events for a specific app.
- [List app event IDs for an app](get-v1-apps-_id_-relationships-appevents.md)
### Getting subscription group and subscription grace period information
- [Read the billing grace period value for an app](get-v1-apps-_id_-subscriptiongraceperiod.md)
  Get the Boolean value that represents the grace period opt-in state for your app.
- [List all subscription groups for an app](get-v1-apps-_id_-subscriptiongroups.md)
  Get a list of subscription groups for a specific app.
- [Get the subscription grace period ID for an app](get-v1-apps-_id_-relationships-subscriptiongraceperiod.md)
- [List subscription group IDs for an app](get-v1-apps-_id_-relationships-subscriptiongroups.md)
### Getting in-app purchase information
- [List all in-app purchases for an app](get-v1-apps-_id_-inapppurchasesv2.md)
  Get a list of the in-app purchases for a specific app.
- [List in-app purchases ids for an app](get-v1-apps-_id_-relationships-inapppurchasesv2.md)
  Get a list of all in-app purchases IDs for a specific app.
- [List all in-app purchases for an app v1](get-v1-apps-_id_-inapppurchases.md)
  List the in-app purchases that are available for your app.
- [List in-app purchases ids for an app v1](get-v1-apps-_id_-relationships-inapppurchases.md)
  Get a list of all in-app purchases IDs for a specific app V1.
### Getting beta feedback
- [List All Beta Feedback Crash Submissions for an App](get-v1-apps-_id_-betafeedbackcrashsubmissions.md)
  Get the beta feedback crash submissions for a specific app.
- [List All Beta Feedback Screenshot Submissions for an App](get-v1-apps-_id_-betafeedbackscreenshotsubmissions.md)
  Get beta feedback screenshot submissions for a specific app.
### Getting background asset information
- [List all background assets for an app](get-v1-apps-_id_-backgroundassets.md)
  Get information about the Apple-hosted background assets for a specific app.
- [List the assets packs ids for an app](get-v1-apps-_id_-relationships-backgroundassets.md)
  Get a list of the Apple hosted background asset IDs for a specific app.
- [Modify a Background Asset](patch-v1-backgroundassets-_id_.md)
  Update a specific background asset.
### Getting alternative distribution information
- [Read an App’s Alternative Distribution Key](get-v1-apps-_id_-alternativedistributionkey.md)
  Get the alternative distribution keys for a specific app.
- [Get the alternative distribution key ID for an app](get-v1-apps-_id_-relationships-alternativedistributionkey.md)
- [Read the marketplace search detail url](get-v1-apps-_id_-marketplacesearchdetail.md)
  Get search detail URL for the alternative marketplace.
- [Get the marketplace search detail ID for an app](get-v1-apps-_id_-relationships-marketplacesearchdetail.md)
### Getting accessibility declaration information
- [List All Accessibility Declarations for an App](get-v1-apps-_id_-accessibilitydeclarations.md)
  Get a list of the accessibility declarations for a specific app.
- [List accessibility declaration IDs for an app](get-v1-apps-_id_-relationships-accessibilitydeclarations.md)
### Getting analytics report request information
- [Read Report Requests](get-v1-apps-_id_-analyticsreportrequests.md)
  Read analytics report requests for a specific app.
- [List analytics report request IDs for an app](get-v1-apps-_id_-relationships-analyticsreportrequests.md)
### Getting webhook information
- [Read Webhook Information for an App](get-v1-apps-_id_-webhooks.md)
  Read webhook configuration details for a specific app.
- [List webhook IDs for an app](get-v1-apps-_id_-relationships-webhooks.md)
### Search keywords
- [List search keyword IDs for an app](get-v1-apps-_id_-relationships-searchkeywords.md)
  Get a list of search keyword IDs for a specific app.
- [List all search keywords for an app](get-v1-apps-_id_-searchkeywords.md)
  Get search keywords for a specific app.
### Getting Game Center detail information
- [Read the state of game center for an app](get-v1-apps-_id_-gamecenterdetail.md)
  Get Game Center detail information for an app.
- [Get the Game Center detail ID for an app](get-v1-apps-_id_-relationships-gamecenterdetail.md)
- [List Game Center-enabled version IDs for an app](get-v1-apps-_id_-relationships-gamecenterenabledversions.md)
### Getting Android to iOS app mapping information
- [Read the Android to iOS App Mapping Details for an App](get-v1-apps-_id_-androidtoiosappmappingdetails.md)
  Get details about the Android to iOS app mapping for a specific app.
- [List the IDs of Android to iOS App Mapping Details for an App](get-v1-apps-_id_-relationships-androidtoiosappmappingdetails.md)
  Get the IDs of Android to iOS app mapping details for a specific app.
### Objects and data types
- [object App](app.md)
  An app registered in App Store Connect, representing all versions, metadata, and configuration for your iOS, macOS, tvOS, or watchOS application.
- [object AppWithoutIncludesResponse](appwithoutincludesresponse.md)
  A response containing a single app, without including related resources.
- [object AppsWithoutIncludesResponse](appswithoutincludesresponse.md)
  A response containing a list of apps, without including related resources.
- [object AppUpdateRequest](appupdaterequest.md)
  The request body you use to update an App Update.
- [object AppClipsResponse](appclipsresponse.md)
  The response body for endpoints that list App Clips for an app.
- [object AppResponse](appresponse.md)
  The response body for endpoints that read or modify a single app in your team.
- [object AppsResponse](appsresponse.md)
  A response containing a list of apps registered in your App Store Connect team.
- [object InAppPurchase](inapppurchase.md)
  A one-time purchasable item available in an app, such as a consumable, non-consumable, or non-renewing subscription.
- [object InAppPurchaseResponse](inapppurchaseresponse.md)
  The response body for endpoints that read a single in-app purchase.
- [object InAppPurchasesResponse](inapppurchasesresponse.md)
  The response body for endpoints that list in-app purchases for an app.
- [object AppBetaTestersLinkagesRequest](appbetatesterslinkagesrequest.md)
  A request body you use to remove beta testers from an app.
- [object AppPricePointV3](apppricepointv3.md)
  A specific price tier in App Store pricing, defining the customer price and developer proceeds across territories.
- [object AppPricePointV3Response](apppricepointv3response.md)
  A response containing a single App Store price point with its territory-specific pricing details.
- [object AppPricePointsV3Response](apppricepointsv3response.md)
  A response containing a list of available App Store price points.
- [object AppPriceSchedule](apppriceschedule.md)
  The pricing schedule for an app, specifying base territory prices, manual prices for other territories, and scheduled price changes.
- [object AppPriceScheduleCreateRequest](apppriceschedulecreaterequest.md)
  The request body you use to create an app price schedule.
- [object AppPriceScheduleResponse](apppricescheduleresponse.md)
  A response containing a single app pricing schedule with its territory configurations.
- [object AppPriceV2](apppricev2.md)
  A price configured for an app in a specific App Store territory under the v2 pricing model.
- [object AppPriceV2InlineCreate](apppricev2inlinecreate.md)
  An inline object for specifying a territory-specific price when creating or updating an app price schedule.
- [object AppPricesV2Response](apppricesv2response.md)
  A response containing a list of territory-specific app prices.
- [object TerritoryInlineCreate](territoryinlinecreate.md)
  An inline object for specifying a territory reference within a parent create or update request.
- [type Platform](platform.md)
  Strings that represent Apple operating systems.
- [type SubscriptionStatusUrlVersion](subscriptionstatusurlversion.md)
  Strings that represent versions of App Store Server Notifications.
- [object App.Relationships.InAppPurchases](app/relationships-data.dictionary/inapppurchases-data.dictionary.md)
  The data and links that describe the relationship between the resources.
- [object AppAlternativeDistributionKeyLinkageResponse](appalternativedistributionkeylinkageresponse.md)
- [object AppWebhooksLinkagesResponse](appwebhookslinkagesresponse.md)
- [object AppAppClipsLinkagesResponse](appappclipslinkagesresponse.md)
- [object AppAppCustomProductPagesLinkagesResponse](appappcustomproductpageslinkagesresponse.md)
- [object AppAppEncryptionDeclarationsLinkagesResponse](appappencryptiondeclarationslinkagesresponse.md)
- [object AppAppEventsLinkagesResponse](appappeventslinkagesresponse.md)
- [object AppAppInfosLinkagesResponse](appappinfoslinkagesresponse.md)
- [object AppAppPricePointsLinkagesResponse](appapppricepointslinkagesresponse.md)
- [object AppAppPriceScheduleLinkageResponse](appapppriceschedulelinkageresponse.md)
- [object AppAppStoreVersionExperimentsV2LinkagesResponse](appappstoreversionexperimentsv2linkagesresponse.md)
- [object AppAppStoreVersionsLinkagesResponse](appappstoreversionslinkagesresponse.md)
- [object AppAvailabilityV2TerritoryAvailabilitiesLinkagesResponse](appavailabilityv2territoryavailabilitieslinkagesresponse.md)
- [object AppBackgroundAssetsLinkagesResponse](appbackgroundassetslinkagesresponse.md)
  A response containing the resource identifiers of background asset versions linked to an app.
- [object BackgroundAssetUpdateRequest](backgroundassetupdaterequest.md)
  The request body you use to update a background asset.
- [object AppBetaAppLocalizationsLinkagesResponse](appbetaapplocalizationslinkagesresponse.md)
- [object AppBetaAppReviewDetailLinkageResponse](appbetaappreviewdetaillinkageresponse.md)
- [object AppBetaFeedbackCrashSubmissionsLinkagesResponse](appbetafeedbackcrashsubmissionslinkagesresponse.md)
- [object AppBetaFeedbackScreenshotSubmissionsLinkagesResponse](appbetafeedbackscreenshotsubmissionslinkagesresponse.md)
- [object AppBetaGroupsLinkagesResponse](appbetagroupslinkagesresponse.md)
- [object AppBetaLicenseAgreementLinkageResponse](appbetalicenseagreementlinkageresponse.md)
- [object AppBuildsLinkagesResponse](appbuildslinkagesresponse.md)
- [object AppCategoryParentLinkageResponse](appcategoryparentlinkageresponse.md)
- [object AppCategorySubcategoriesLinkagesResponse](appcategorysubcategorieslinkagesresponse.md)
- [object AppCiProductLinkageResponse](appciproductlinkageresponse.md)
- [object AppCustomProductPageAppCustomProductPageVersionsLinkagesResponse](appcustomproductpageappcustomproductpageversionslinkagesresponse.md)
  A response containing the resource identifiers of versions for a custom App Store product page.
- [object AppEndUserLicenseAgreementLinkageResponse](appenduserlicenseagreementlinkageresponse.md)
- [object AppGameCenterDetailLinkageResponse](appgamecenterdetaillinkageresponse.md)
- [object AppGameCenterEnabledVersionsLinkagesResponse](appgamecenterenabledversionslinkagesresponse.md)
- [object AppInAppPurchasesLinkagesResponse](appinapppurchaseslinkagesresponse.md)
- [object AppInAppPurchasesV2LinkagesResponse](appinapppurchasesv2linkagesresponse.md)
- [object AppInfoAgeRatingDeclarationLinkageResponse](appinfoageratingdeclarationlinkageresponse.md)
- [object AppInfoAppInfoLocalizationsLinkagesResponse](appinfoappinfolocalizationslinkagesresponse.md)
- [object AppInfoPrimaryCategoryLinkageResponse](appinfoprimarycategorylinkageresponse.md)
- [object AppInfoPrimarySubcategoryOneLinkageResponse](appinfoprimarysubcategoryonelinkageresponse.md)
- [object AppInfoPrimarySubcategoryTwoLinkageResponse](appinfoprimarysubcategorytwolinkageresponse.md)
- [object AppInfoSecondaryCategoryLinkageResponse](appinfosecondarycategorylinkageresponse.md)
- [object AppInfoSecondarySubcategoryOneLinkageResponse](appinfosecondarysubcategoryonelinkageresponse.md)
- [object AppInfoSecondarySubcategoryTwoLinkageResponse](appinfosecondarysubcategorytwolinkageresponse.md)
- [object AppMarketplaceSearchDetailLinkageResponse](appmarketplacesearchdetaillinkageresponse.md)
- [object AppPerfPowerMetricsLinkagesResponse](appperfpowermetricslinkagesresponse.md)
- [object AppPreReleaseVersionsLinkagesResponse](appprereleaseversionslinkagesresponse.md)
- [object AppPricePointV3EqualizationsLinkagesResponse](apppricepointv3equalizationslinkagesresponse.md)
- [object AppPriceScheduleAutomaticPricesLinkagesResponse](apppricescheduleautomaticpriceslinkagesresponse.md)
- [object AppPriceScheduleBaseTerritoryLinkageResponse](apppriceschedulebaseterritorylinkageresponse.md)
- [object AppPriceScheduleManualPricesLinkagesResponse](apppriceschedulemanualpriceslinkagesresponse.md)
- [object AppReviewSubmissionsLinkagesResponse](appreviewsubmissionslinkagesresponse.md)
  A response containing the resource identifiers of review submissions associated with an app.
- [object AppSearchKeywordsLinkagesResponse](appsearchkeywordslinkagesresponse.md)
  A response containing the resource identifiers of search keywords associated with an app.
- [type OfferCodeEnvironment](offercodeenvironment.md)
  A string that represents the environment of an offer code.
- [type TerritoryCode](territorycode.md)
  The App Store territory codes.

## See Also

- [App Metadata](app-metadata.md)
  Manage the metadata of apps in App Store Connect.
- [Custom Product Pages and Localizations](custom-product-pages-and-localizations.md)
  Create and manage your app’s custom product pages and localizations.
- [App Events and Metadata](app-events-and-metadata.md)
  Create and schedule in-app events and manage in-app event metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/apps)*