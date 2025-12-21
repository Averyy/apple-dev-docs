# ageRatingCode

**Framework**: StoreKit  
**Kind**: property

The current age rating code for your app.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- macOS 26.2+
- tvOS 26.2+
- visionOS 26.2+
- watchOS 26.2+

## Declaration

```swift
static var ageRatingCode: Int? { get async }
```

#### Return Value

An integer representing the current age rating code, or `nil` if the age rating is unavailable.

#### Discussion

Use this property to fetch the age rating for your app and compare it with the last known age rating to check if it has changed.

The following is an example of getting the age rating for an app:

```swift
func getAgeRatingCode() async -> Int? {
    guard let ageRatingCode = await AppStore.ageRatingCode else {
        print("Age rating code unavailable")
        return nil
    }
    return ageRatingCode
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/ageratingcode)*