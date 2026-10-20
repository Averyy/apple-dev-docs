# Providing age-rating appropriate content

**Framework**: MarketplaceKit  
**Role**: Article

Check for age-rating based content restrictions and enable people to request approval for apps with a rating beyond the maximum allowed for the device.

#### Overview

You can help create a browsing experience consistent with the device’s maximum allowed age rating. When a person tries to install an app that has an age rating beyond the maximum allowed for the device, present a framework-provided sheet that enables the person to request the approval of a parent or guardian to install the app. The sheet contains an Ask for Exception button, which when tapped, sends a message to the parent or guardian.

![An iPhone device body that features a modal sheet for the Ask for Exception workflow. Text notifies the person that a parent or guardian needs to approve the installation of an app that's rated 13+ named Social Media by Tapland, Inc. from the Megabyte Mart marketplace. Two buttons follow the text. The top button's label is Ask for Exception, the bottom button's label is Cancel.](https://developer.apple.com/tutorials/images/com.apple.MarketplaceKit/providing-age-rating-appropriate-content-1@2x.png)

![An iPhone device body that features the Messages app with a unsent message that reads Request from Child. The message contains additional text that describes the app, its age rating, and the marketplace that distributes the app.](https://developer.apple.com/tutorials/images/com.apple.MarketplaceKit/providing-age-rating-appropriate-content-2@2x.png)

When the parent or guardian taps the message, a sheet displays with buttons to approve or decline the request.

![An iPhone device body that features the Messages app with a recieved message that reads Request from Child. The message describes the app installation exception request and names the app, its age rating, and the marketplace that distributes the app.](https://developer.apple.com/tutorials/images/com.apple.MarketplaceKit/providing-age-rating-appropriate-content-3@2x.png)

![An iPhone device body that features a modal sheet for the Ask for Exception workflow. Text notifies the person that a child needs approval to download an app that's rated 13+ named Social Media by Tapland, Inc. from the Megabyte Mart marketplace. Two buttons follow the text. The top button's label is Approve, the bottom button's label is Decline.](https://developer.apple.com/tutorials/images/com.apple.MarketplaceKit/providing-age-rating-appropriate-content-4@2x.png)

Alternatively, if the request recipient is in the vicinity of the device, a follow-on pane for the request flow contains an Approve in Person button, which when tapped, approves the request after the parent or guardian authenticates with their Apple Account.

![An iPhone device body that features a modal sheet for the Ask for Exception workflow. Text notifies the person that the request message is sent and pending approval, and that a parent or guardian can approve the request in person if they're in the vicinity of the device. Two buttons follow the text that read Approve in Person and Close.](https://developer.apple.com/tutorials/images/com.apple.MarketplaceKit/providing-age-rating-appropriate-content-5@2x.png)

#### Check for age-rating based content restrictions

When people browse apps on your alternative app marketplace, you can check the [`maximumAllowedAgeRating`](./applibrary/maximumallowedagerating.md) property for any age-rating based restrictions set for the device. By adjusting your presentation of content that’s rated higher than the maximum allowed for the device, you can create a more age-rating appropriate browsing experience. For example, you can omit articles or featured content for rating-restricted apps but still return rating-restricted apps in search results to allow someone to request an exception to install one.

When a person tries to install an app that has an age rating beyond the maximum allowed for the device, set the [`requestAgeException`](./installmetadata/requestageexception.md) property to `true`, such as through the [`init(account:appleItemID:alternativeDistributionPackage:isUpdate:appShareURL:requestAgeException:)`](./installmetadata/init%28account,appleitemid,alternativedistributionpackage,isupdate,appshareurl,requestageexception%29.md) initializer. This presents the Ask for Exception sheet and queues the app as a pending age-rating exception request in the [`currentAgeExceptionRequests()`](./applibrary/currentageexceptionrequests%28%29.md) list. The framework also throws [`MarketplaceKitError.cancelled`](./marketplacekiterror/cancelled.md), because it doesn’t install the app at this time.

If the app to install has an age rating beyond the maximum allowed for the device and your app fails to request an age-rating exception, the framework throws [`MarketplaceKitError.ratingRestricted`](./marketplacekiterror/ratingrestricted.md). Conversely, if your app requests an age-rating exception by setting [`requestAgeException`](./installmetadata/requestageexception.md) to `true` when it’s not needed, the framework throws [`MarketplaceKitError.ageRatingExceptionNotNeeded`](./marketplacekiterror/ageratingexceptionnotneeded.md).

#### Show exception status and enable in-person approval

While an exception is pending, check the request status in the [`currentAgeExceptionRequests()`](./applibrary/currentageexceptionrequests%28%29.md) property of the [`AppLibrary`](./applibrary.md) class. For apps that are pending an exception, you can show a Pending button rather than an Install button.

If a parent or guardian is present, enable a person to present the exception sheet again by calling the [`presentAgeExceptionApproveInPersonSheet()`](./applibrary/app/presentageexceptionapproveinpersonsheet%28%29.md) method of the [`AppLibrary.App`](./applibrary/app.md) class. For example, you can display an Approve Now button next to the pending app. The sheet contains an Approve in Person button which, when tapped, requires the parent or guardian to authenticate with their Apple Account before the system installs the app.

If your app calls [`presentAgeExceptionApproveInPersonSheet()`](./applibrary/app/presentageexceptionapproveinpersonsheet%28%29.md) when there’s no age-rating exception requests for the app in [`currentAgeExceptionRequests()`](./applibrary/currentageexceptionrequests%28%29.md), the framework throws [`MarketplaceKitError.missingAgeRatingExceptionRequest`](./marketplacekiterror/missingageratingexceptionrequest.md).

## See Also

### Authorization
- [Reauthenticating a person to manage apps](./reauthenticating-a-person-to-manage-apps.md)
  Renew your app’s authorization when an app needs updating or when a device restores from backup.
- [com.apple.developer.marketplace.app-installation](../BundleResources/entitlements/com.apple.developer.marketplace.app-installation.md)
  An entitlement that enables an app to vend other apps as an alternative app marketplace.
- [com.apple.developer.browser.app-installation](../BundleResources/entitlements/com.apple.developer.browser.app-installation.md)
  An entitlement that enables a browser to install alternative distribution apps from a website.
- [App License Delivery SDK](../AppLicenseDeliverySDK/AppLicenseDeliverySDK.md)
  Secure the installation of alternative distribution apps on iOS or iPadOS devices by vending licenses from your web server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/providing-age-rating-appropriate-content)*