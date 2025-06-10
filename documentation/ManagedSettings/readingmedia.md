# Confirming the Effective TV and Movie Ratings

**Framework**: ManagedSettings

Read the media rating on a device and determine what media to display on your app.

#### Overview

The parental control app sets the media rating that establishes the parameters of the content the user can view. Your app reads the rating to determine what media to display, so you don’t need to incorporate monitoring with [`DeviceActivity`](https://developer.apple.com/documentation/DeviceActivity) or authorize your app through [`FamilyControls`](https://developer.apple.com/documentation/FamilyControls).

##### Read the Media Setting

To access the media setting, first create a [`ManagedSettingsStore`](managedsettingsstore.md) object.

The following code shows how to get the current movie rating settings on a device:

```swift
let store = ManagedSettingsStore()
// Access the ManagedSettingsStore.

switch(store.effectiveMaximumMovieRating) {
case 1000: 
// Show all content.
case 300:
// Show content up through PG-13.
// And so on.
}
```

This code example identifies the maximum movie rating the user can view on their device. This number can range from `0-1000`. A device that has no predetermined settings prints `1000` to mean all media can be viewed. The number `0` indicates that the user can’t view any movies. To learn more about what each rating means for your app, see [`maximumMovieRating`](mediasettings/maximummovierating-swift.property.md).

> **Note**: Because your app only reads media settings, you don’t need to request `Family Controls` authorization from the user or monitor device activity.

While the example above shows how to view the maximum movie ratings, the example can translate to checking the effective maximum TV show ratings as well.

The following code example shows how to get the current TV show rating on a device:

```swift
let store = ManagedSettingsStore()
// Access the ManagedSettingsStore.

switch(store.effectiveMaximumTVRating) {
case 1000: 
// Show all content.
case 300:
// Show content up through TV-G.
// And so on.
}
```

> **Note**: Both [`effectiveMaximumMovieRating`](managedsettingsstore/effectivemaximummovierating.md) and [`effectiveMaximumTVShowRating`](managedsettingsstore/effectivemaximumtvshowrating.md) are `@Published` and can change at any time. Keep track of the changes to these properties in your media app.

##### Monitor the Effective Rating

The parental controls app can change the effective rating at any time. To reflect the changes, make sure to incorporate them into your media app. Use publishers to subscribe to updates on changes to a rating. Managed Settings uses [`$effectiveMaximumMovieRating`](managedsettingsstore/$effectivemaximummovierating.md) and [`$effectiveMaximumTVShowRating`](managedsettingsstore/$effectivemaximumtvshowrating.md) to publish to media changes.

The following code example shows how to subscribe for changes to `$effectiveMaximumMovieRating`:

```swift
let maximumMovieRating = store.effectiveMaximumMovieRating
// Read the effective media setting.

// Subscribe for changes.
self.movieRatingCancellable = store.$effectiveMaximumMovieRating.sink { effectiveMaximumMovieRating in
// Handle the change to effectiveMaximumMovieRating.
}
```

> ❗ **Important**: Use the [`Family Controls`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.family-controls) entitlement in your app to subscribe for TV and Movie rating changes. For more information on how to set up entitlements, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

## See Also

- [Manage Settings on Devices in a Family Sharing Group](connectionwithframeworks.md)
  Empower parents and guardians to configure constraints on other devices while preserving the family’s privacy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/readingmedia)*