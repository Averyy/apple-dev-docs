# Tip.Event

**Framework**: Tipkit  
**Kind**: typealias

A repeatable user-defined action.

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
typealias Event = Tips.Event
```

#### Overview

Use an event when you want to track an action that can occur one or more times in your app (such as a user logging in). Then use [`donate()`](tips/event/donate().md) to donate to the event when the action occurs, increasing the event count by one.

> **Note**: In order to remain performant, by default events only query their most recent 1000 donations.

##### Creating an Event with No Associated Donation Value

The example below creates a `landmarksAppDidOpen` event with no associated donation value and donates it anytime `ContentView` appears:

```swift
struct LandmarkTips: App {
    static let landmarksAppDidOpen = Tips.Event(id: "landmarksAppDidOpen")

    var body: some Scene {
        WindowGroup {
            ContentView()
                .onAppear { Self.landmarksAppDidOpen.sendDonation() }
        }
    }
}
```

The example below creates a display rule for `LandmarkFeatureTip` based on the `landmarksAppDidOpen` event.

```swift
struct LandmarkFeatureTip: Tip {
    var rules: [Rule] {
        // Tip will only display when the landmarksAppDidOpen event has been donated 3 or more times in the last week.
        #Rule(LandmarkTips.landmarksAppDidOpen) {
            $0.donations.donatedWithin(.week).count >= 3
        }
    }
}
```

##### Creating an Event with an Associated Donation Value

The example below creates a `didViewLandmarkDetail` event with an associated donation value and donates it anytime the `LandmarkDetail` appears:

```swift
struct LandmarkDetail: View {
    static let didViewLandmarkDetail = Tips.Event<DidViewLandmark>(id: "didViewLandmarkDetail")

    struct DidViewLandmark: Codable, Sendable {
        let landmarkID: Int
        let landmarkName: String
    }

    var landmark: Landmark

    var body: some View {
        ScrollView {
            MapView(coordinate: landmark.locationCoordinate)
        }
        .onAppear {
            Self.didViewLandmarkDetail.sendDonation(.init(landmarkID: landmark.id, landmarkName: landmark.name))
        }
    }
}
```

The example below creates a display rule for `LandmarkDetailTip` based on the `didViewLandmarkDetail` event.

```swift
struct LandmarkDetailTip: Tip {
    var rules: [Rule] {
        // Tip will only display when the didViewLandmarkDetail has been donated 3 or more times for landmarks not named "Wilbere Bowl".
        #Rule(LandmarkDetail.didViewLandmarkDetail) {
            $0.donations.filter({ $0.landmarkName != "Wilbere Bowl" }).count > 3
        }
    }
}
```

## Topics

### Initializer
- [init(id: String)](tips/event/init(id:).md)
  Creates an event with the specified identifier.
### Properties
- [var donations: [Tips.Event<DonationInfo>.Donation]](tips/event/donations.md)
### Add Donations
- [func donate() async](tips/event/donate.md)
  Donates an event with no associated `Donation` value.
- [func donate(DonationInfo) async](tips/event/donate(_:).md)
  Donates an event along with its associated `Donation` value.
- [func sendDonation((() -> Void)?)](tips/event/senddonation(_:).md)
  Asynchronously donates an event with no associated `Donation` value.
- [func sendDonation(DonationInfo, (() -> Void)?)](tips/event/senddonation(_:_:).md)
  Asynchronously donates an event along with its associated `Donation` value.
### Creating rules
- [struct Rule](tips/rule.md)
  A condition to meet before displaying a tip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tip/event)*