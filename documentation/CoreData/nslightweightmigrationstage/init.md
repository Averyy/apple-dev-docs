# init(_:)

**Framework**: Core Data  
**Kind**: init

Creates a lightweight migration stage with the specified version checksums.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+
- Swift 5.8+

## Declaration

```swift
convenience init(_ checksums: [String])
```

#### Discussion

To determine an object model’s version checksum, use its [`versionChecksum`](nsmanagedobjectmodel/versionchecksum.md) property. Alternatively, you can find the checksum in the versioned model’s `VersionInfo.plist` file or in Xcode’s build log.

## Parameters

- `checksums`: The array of version checksums.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nslightweightmigrationstage/init(_:))*