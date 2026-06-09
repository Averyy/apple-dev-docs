# Upgrading to Apple School Manager and Apple Business Manager

**Framework**: Device Management

Manage devices and content across an organization’s user base with a single destination.

#### Overview

[`Apple School Manager`](https://developer.apple.comhttps://www.apple.com/education/) and [`Apple Business Manager`](https://developer.apple.comhttps://www.apple.com/business/it/) enable content managers to purchase content in the same place that they manage Apple Accounts and devices. You can automate device deployment, purchase and distribute content, and manage roles in your organization. Apple School Manager and Apple Business Manager work seamlessly with your device management service to make it easy to enroll devices, deploy content, and delegate administrative privileges.

#### Upgrade to Support Location Based Tokens

The purchases you make in VPP in Apple School Manager and Apple Business Manager are location-based, making it easy for content managers to move licenses between locations as needed. Upgrading to location-based tokens is strongly recommended, but optional. Update your device management service to support location-based tokens as follows:

1. Update API calls to handle the `location` field that returns. Licenses assigned with a legacy token don’t have a location. All assets you purchase with VPP in Apple School Manager or Apple Business Manager have an additional `location` field in their API responses.
2. Update your UI to show location names for tokens and assets. Location names aren’t unique (many schools may have the same name), but location UIDs are unique to a specific location. Displaying the location name to the user is particularly important when the location token is about to expire.
3. Refresh license status at appropriate times (each page load) to maintain an accurate UI. Because you can reallocate licenses in Apple School Manager and Apple Business Manager, license counts change outside the device management service.
4. Use [`Get Assets`](get-assets-44p83.md) not [`Get Licenses`](get-licenses.md) to get license counts. [`Get Assets`](get-assets-44p83.md) is more efficient and returns an aggregation of `adamId` values and counts, instead of all the individual licenses.
5. Handle the case when duplicate tokens are uploaded by different content managers. There is just one location token that needs to be stored, instead of a token per VPP account. The `uId` field is a unique library identifier that’s included in all API responses. When querying assets using multiple tokens that may share libraries, use the `uId` field to filter duplicates.
6. Handle any new errors related to location-based tokens.

> ⚠️ **Warning**:  Licenses assigned using a legacy token must continue to be managed by the legacy token until you transfer them to a location. Device management services need to support both models of licensing simultaneously. Failure to support both the legacy and location-based models of tokens creates discrepancies between user experiences in Apple School Manager and Apple Business Manager and their device management service.

## See Also

- [Getting app and book information (Legacy)](getting-app-and-book-information-legacy.md)
  Use a web service to find details about apps and books to show to your users.
- [Managing apps and books through web services (Legacy)](managing-apps-and-books-through-web-services-legacy.md)
  Associate volume purchases with users or devices using endpoints provided by the Volume Purchase Program (VPP).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/upgrading-to-apple-school-manager-and-apple-business-manager)*