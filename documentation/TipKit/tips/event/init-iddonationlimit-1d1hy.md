# init(id:donationLimit:)

**Framework**: TipKit  
**Kind**: init

Creates an event with an associated donation value.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(id: String, donationLimit: Tips.DonationLimit)
```

##### Creating an Event

Create an event when you want display a tip based on an action that can occur one or more times in your app (such as a user logging in). Then use [`donate()`](tips/event/donate().md) to donate to the event when the action occurs, increasing the event count by one.

```swift
struct LandmarkDetailView: View {
    let landmark: Landmark

    var body: some View {
        VStack {
            Text(landmark.name)
            Text(landmark.description)
        }
        .task {
            let donationInfo = DidViewLandmark(landmarkName: landmark.name)
            await Self.didViewLandmark.donate(donationInfo)
        }
    }

    static let didViewLandmark = Event(id: "didViewLandmark")
}
```

##### Adding Event Rules

Add tip display rules using the `#Rule` macro to prevent a tip from being displayed until an event has been donated a specific number of times.

```swift
struct FavoriteLandmarkTip: Tip {
    var rules: [Rule] {
        // Tip will only display when the didViewLandmark event has been donated 3 or more times.
        #Rule(LandmarkDetailView.didViewLandmark) {
            $0.donations.count >= 3
        }
    }
}
```

## Parameters

- `id`: Unique identifier for persisting the event and its donations.
- `donationLimit`: Maximum number and maximum age of donations this event will persist and query.

## Topics

### Properties
- [var donations: [Tips.Event<DonationInfo>.Donation]](tips/event/donations.md)
  Returns an events existing donations.
### Add Donations
- [func donate() async](tips/event/donate.md)
  Donates an event with no associated `Donation` value.
- [func donate(DonationInfo) async](tips/event/donate(_:).md)
  Donates an event along with its associated `Donation` value.
- [func sendDonation((() -> Void)?)](tips/event/senddonation(_:).md)
  Asynchronously donates an event with no associated `Donation` value.
- [func sendDonation(DonationInfo, (() -> Void)?)](tips/event/senddonation(_:_:).md)
  Asynchronously donates an event along with its associated `Donation` value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/event/init(id:donationlimit:)-1d1hy)*