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
- [Read an app’s encryption declaration IDs](get-v1-apps-_id_-relationships-appencryptiondeclarations.md)
  Find and list all available app encryption declaration IDs for a specific app.
### Getting app build and prerelease version information
- [List All Builds of an App](get-v1-apps-_id_-builds.md)
  Get a list of builds associated with a specific app.
- [GET /v1/apps/{id}/relationships/builds](get-v1-apps-_id_-relationships-builds.md)
- [List All Prerelease Versions for an App](get-v1-apps-_id_-prereleaseversions.md)
  Get a list of prerelease versions associated with a specific app.
- [GET /v1/apps/{id}/relationships/preReleaseVersions](get-v1-apps-_id_-relationships-prereleaseversions.md)
### Getting App Clip information
- [List All App Clips for an App](get-v1-apps-_id_-appclips.md)
  List your app’s associated App Clips.
- [GET /v1/apps/{id}/relationships/appClips](get-v1-apps-_id_-relationships-appclips.md)
### Getting beta tester information for TestFlight
- [List All Beta Groups for an App](get-v1-apps-_id_-betagroups.md)
  Get a list of beta groups associated with a specific app.
- [GET /v1/apps/{id}/relationships/betaGroups](get-v1-apps-_id_-relationships-betagroups.md)
- [Remove Specified Beta Testers from All Groups and Builds of an App](delete-v1-apps-_id_-relationships-betatesters.md)
  Remove one or more beta testers’ access to test any builds of a specific app.
### Getting an app’s TestFlight details
- [Read the Beta App Review Details Resource of an App](get-v1-apps-_id_-betaappreviewdetail.md)
  Get the beta app review details for a specific app.
- [GET /v1/apps/{id}/relationships/betaAppReviewDetail](get-v1-apps-_id_-relationships-betaappreviewdetail.md)
- [GET /v1/apps/{id}/relationships/betaAppReviewDetail](get-v1-apps-_id_-relationships-betaappreviewdetail.md)
- [Read the Beta License Agreement of an App](get-v1-apps-_id_-betalicenseagreement.md)
  Get the beta license agreement for a specific app.
- [GET /v1/apps/{id}/relationships/betaLicenseAgreement](get-v1-apps-_id_-relationships-betalicenseagreement.md)
- [List All Beta App Localizations of an App](get-v1-apps-_id_-betaapplocalizations.md)
  Get a list of localized beta test information for a specific app.
- [GET /v1/apps/{id}/relationships/betaAppLocalizations](get-v1-apps-_id_-relationships-betaapplocalizations.md)
### Getting an app’s Xcode Cloud products
- [Read the Xcode Cloud Product for an App](get-v1-apps-_id_-ciproduct.md)
  Get the Xcode Cloud product information for an app you build with Xcode Cloud.
- [GET /v1/apps/{id}/relationships/ciProduct](get-v1-apps-_id_-relationships-ciproduct.md)
### Getting an app’s price points
- [List all price points for an app](get-v1-apps-_id_-apppricepoints.md)
  Get all the available price points for a specific app.
- [GET /v1/apps/{id}/relationships/appPricePoints](get-v1-apps-_id_-relationships-apppricepoints.md)
- [Read app price point information](get-v3-apppricepoints-_id_.md)
  Get details about a specific app price point.
- [List app price point equalizations](get-v3-apppricepoints-_id_-equalizations.md)
  List all equivalent app prices points to a base price point.
- [GET /v3/appPricePoints/{id}/relationships/equalizations](get-v3-apppricepoints-_id_-relationships-equalizations.md)
### Getting App Store details for your app
- [List All App Infos for an App](get-v1-apps-_id_-appinfos.md)
  Get information about an app that is currently live on App Store, or that goes live with the next version.
- [GET /v1/apps/{id}/relationships/appInfos](get-v1-apps-_id_-relationships-appinfos.md)
- [List All App Store Versions for an App](get-v1-apps-_id_-appstoreversions.md)
  Get a list of all App Store versions of an app across all platforms.
- [GET /v1/apps/{id}/relationships/appStoreVersions](get-v1-apps-_id_-relationships-appstoreversions.md)
- [Read the End User License Agreement Information of an App](get-v1-apps-_id_-enduserlicenseagreement.md)
  Get the custom end user license agreement (EULA) for a specific app and the territories where the agreement applies.
- [GET /v1/apps/{id}/relationships/endUserLicenseAgreement](get-v1-apps-_id_-relationships-enduserlicenseagreement.md)
- [List all custom product pages for an app](get-v1-apps-_id_-appcustomproductpages.md)
  Get a list of all custom product pages for a specific app.
- [Get all custom product page resource IDs for an app](get-v1-apps-_id_-relationships-appcustomproductpages.md)
  Get a list of custom product page resource IDs associated with an app.
- [GET /v1/apps/{id}/appStoreVersionExperimentsV2](get-v1-apps-_id_-appstoreversionexperimentsv2.md)
- [GET /v1/apps/{id}/relationships/appStoreVersionExperimentsV2](get-v1-apps-_id_-relationships-appstoreversionexperimentsv2.md)
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
- [List review submission Ids](get-v1-apps-_id_-relationships-reviewsubmissions.md)
  Get the list of review submission IDs for a specific app.
### Getting power and performance metrics
- [Get Power and Performance Metrics for an App](get-v1-apps-_id_-perfpowermetrics.md)
  Get the performance and power metrics data for the most recent version of an app.
### Getting customer reviews
- [List All Customer Reviews for an App](get-v1-apps-_id_-customerreviews.md)
  Get a list of customer reviews for a specific app.
- [GET /v1/apps/{id}/relationships/customerReviews](get-v1-apps-_id_-relationships-customerreviews.md)
- [Read customer review summarizations](get-v1-apps-_id_-customerreviewsummarizations.md)
  Get the customer review summarization for a specific app.
### Getting and managing an app’s price schedules
- [Read price schedule information for an app](get-v1-apps-_id_-apppriceschedule.md)
  Read price schedule details for a specific app.
- [GET /v1/apps/{id}/relationships/appPriceSchedule](get-v1-apps-_id_-relationships-apppriceschedule.md)
- [Read an app's price schedule information](get-v1-apppriceschedules-_id_.md)
  List the price schedule details for a specific app.
- [List automatically generated prices for an app](get-v1-apppriceschedules-_id_-automaticprices.md)
  List the automatically calculated prices for an app generated from a base territory.
- [Read the base territory for an app's price schedule](get-v1-apppriceschedules-_id_-baseterritory.md)
  Read the base territory and currency for a specific app.
- [List manually chosen prices for an app](get-v1-apppriceschedules-_id_-manualprices.md)
  List the prices you chose for a specific app.
- [GET /v1/appPriceSchedules/{id}/relationships/automaticPrices](get-v1-apppriceschedules-_id_-relationships-automaticprices.md)
- [GET /v1/appPriceSchedules/{id}/relationships/baseTerritory](get-v1-apppriceschedules-_id_-relationships-baseterritory.md)
- [GET /v1/appPriceSchedules/{id}/relationships/manualPrices](get-v1-apppriceschedules-_id_-relationships-manualprices.md)
- [Add a scheduled price change to an app](post-v1-apppriceschedules.md)
  Create a scheduled price change for an app.
### Getting and managing an app’s availability
- [List availability for an app](get-v1-apps-_id_-appavailabilityv2.md)
  Get a list of availabilities for a specific app.
- [GET /v1/apps/{id}/relationships/appAvailabilityV2](get-v1-apps-_id_-relationships-appavailabilityv2.md)
### Getting beta tester metrics
- [Read beta tester metrics for an app](get-v1-apps-_id_-metrics-betatesterusages.md)
  Get usage metrics for beta testers of a specific app.
### Getting app event information
- [GET /v1/apps/{id}/appEvents](get-v1-apps-_id_-appevents.md)
- [GET /v1/apps/{id}/relationships/appEvents](get-v1-apps-_id_-relationships-appevents.md)
### Getting subscription group and subscription grace period information
- [Read the Billing Grace Period Value for an App](get-v1-apps-_id_-subscriptiongraceperiod.md)
  Get the Boolean value that represents the grace period opt-in state for your app.
- [List All Subscription Groups for an App](get-v1-apps-_id_-subscriptiongroups.md)
  Get a list of subscription groups for a specific app.
- [GET /v1/apps/{id}/relationships/subscriptionGracePeriod](get-v1-apps-_id_-relationships-subscriptiongraceperiod.md)
- [GET /v1/apps/{id}/relationships/subscriptionGroups](get-v1-apps-_id_-relationships-subscriptiongroups.md)
### Getting in-app purchase information
- [List All In-App Purchases for an App](get-v1-apps-_id_-inapppurchasesv2.md)
  Get a list of the in-app purchases for a specific app.
- [List in-app purchases IDs for an app](get-v1-apps-_id_-relationships-inapppurchasesv2.md)
  Get a list of all in-app purchases IDs for a specific app.
- [List All In-App Purchases for an App V1](get-v1-apps-_id_-inapppurchases.md)
  List the in-app purchases that are available for your app.
- [List in-app purchases IDs for an app V1](get-v1-apps-_id_-relationships-inapppurchases.md)
  Get a list of all in-app purchases IDs for a specific app V1.
### Getting beta feedback
- [List all beta feedback crash submissions for an app](get-v1-apps-_id_-betafeedbackcrashsubmissions.md)
  Get the beta feedback crash submissions for a specific app.
- [List all beta feedback screenshot submissions for an app](get-v1-apps-_id_-betafeedbackscreenshotsubmissions.md)
  Get beta feedback screenshot submissions for a specific app.
### Getting background asset information
- [List all assets packs for an app](get-v1-apps-_id_-backgroundassets.md)
  Get information about the Apple-hosted background assets for a specific app.
- [List the assets packs IDs for an app](get-v1-apps-_id_-relationships-backgroundassets.md)
  Get a list of the Apple hosted background asset IDs for a specific app.
- [Modify a background asset](patch-v1-backgroundassets-_id_.md)
  Update a specific background asset.
### Getting alternative distribution information
- [Read an app’s alternative distribution key](get-v1-apps-_id_-alternativedistributionkey.md)
  Get the alternative distribution keys for a specific app.
- [GET /v1/apps/{id}/relationships/alternativeDistributionKey](get-v1-apps-_id_-relationships-alternativedistributionkey.md)
- [Read the marketplace search detail URL](get-v1-apps-_id_-marketplacesearchdetail.md)
  Get search detail URL for the alternative marketplace.
- [GET /v1/apps/{id}/relationships/marketplaceSearchDetail](get-v1-apps-_id_-relationships-marketplacesearchdetail.md)
### Getting accessibility declaration information
- [List all accessibility declarations for an app](get-v1-apps-_id_-accessibilitydeclarations.md)
  Get a list of the accessibility declarations for a specific app.
- [GET /v1/apps/{id}/relationships/accessibilityDeclarations](get-v1-apps-_id_-relationships-accessibilitydeclarations.md)
### Getting analytics report request information
- [Read report requests](get-v1-apps-_id_-analyticsreportrequests.md)
  Read analytics report requests for a specific app.
- [GET /v1/apps/{id}/relationships/analyticsReportRequests](get-v1-apps-_id_-relationships-analyticsreportrequests.md)
### Getting webhook information
- [Read webhook information for an app](get-v1-apps-_id_-webhooks.md)
  Read webhook configuration details for a specific app.
- [GET /v1/apps/{id}/relationships/webhooks](get-v1-apps-_id_-relationships-webhooks.md)
### Search keywords
- [GET /v1/apps/{id}/relationships/searchKeywords](get-v1-apps-_id_-relationships-searchkeywords.md)
- [GET /v1/apps/{id}/searchKeywords](get-v1-apps-_id_-searchkeywords.md)
### Getting Game Center detail information
- [Read the state of Game Center for an app](get-v1-apps-_id_-gamecenterdetail.md)
  Get Game Center detail information for an app.
- [GET /v1/apps/{id}/relationships/gameCenterDetail](get-v1-apps-_id_-relationships-gamecenterdetail.md)
- [GET /v1/apps/{id}/relationships/gameCenterEnabledVersions](get-v1-apps-_id_-relationships-gamecenterenabledversions.md)
### Getting Android to iOS app mapping information
- [Read the Android to iOS app mapping details for an app](get-v1-apps-_id_-androidtoiosappmappingdetails.md)
  Get details about the Android to iOS app mapping for a specific app.
- [List the IDs of Android to iOS app mapping details for an app](get-v1-apps-_id_-relationships-androidtoiosappmappingdetails.md)
  Get the IDs of Android to iOS app mapping details for a specific app.
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
  A response that contains a list of IDs of related background assets.
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
  A response that contains a list of IDs of related resources.
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
  A response that contains a list of IDs of related resources.
- [object AppSearchKeywordsLinkagesResponse](appsearchkeywordslinkagesresponse.md)
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