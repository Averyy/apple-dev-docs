# init(identifier:)

**Framework**: CloudKit  
**Kind**: init

Creates a container for the specified identifier.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init(identifier containerIdentifier: String)
```

#### Discussion

The specified identifier must correspond to one of the ubiquity containers in the iCloud capabilities section of your Xcode project. Including the identifier with your app’s capabilities adds the corresponding entitlements to your app. To access your app’s default container, use the [`default()`](ckcontainer/default().md) method instead.

## Parameters

- `containerIdentifier`: The bundle identifier of the app with the container that you want to access. The bundle identifier must be in the app’s   entitlement. This parameter must not be  .

## See Also

- [class func `default`() -> CKContainer](ckcontainer/default.md)
  Returns the app’s default container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/init(identifier:))*