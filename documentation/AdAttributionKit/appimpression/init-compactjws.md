# init(compactJWS:)

**Framework**: AdAttributionKit  
**Kind**: init

Creates a new app impression with the provided compact JSON Web Signature (JWS).

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst ?+

## Declaration

```swift
init(compactJWS: String) async throws
```

#### Discussion

Create a new `AppImpression` by providing a compact string representation of the JWS as the following example shows:

```swift
    do {
        let impression = try await AppImpression(compactJWS: compactJWS)
        print("Impression advertised item ID: \(impression.advertisedItemID)")
    }
    catch {
        print("Failed to decode impression: \(error)")
    }
```

## Parameters

- `compactJWS`: A string that represents a JWS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/appimpression/init(compactjws:))*