# url(_:)

**Framework**: TipKit  
**Kind**: method

Configuration option for persisting tips at a custom on-disk location.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static func url(_ url: URL) -> Tips.ConfigurationOption.DatastoreLocation
```

#### Discussion

```swift
do {
    let tipsDatastoreLocation = URL.applicationSupportDirectory.appendingPathComponent("LandmarkTips")
    // Save the tips datastore at the specified URL.
    try Tips.configure([
        .datastoreLocation(.url(tipsDatastoreLocation))
    ])
}
catch {
    print("Error initializing TipKit \(error)")
}
```

## Parameters

- `url`: URL for on-disk location of the tips datastore.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/configurationoption/datastorelocation/url(_:))*