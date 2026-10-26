# localIdentifierMappingsForSyncedCloudIdentifiers:

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Returns a dictionary that maps each cloud identifier from the provided array to a `PHLocalIdentifierMapping` result containing the local identifier found for that cloud identifier if that cloud identifier is a known synced identifier.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
- (NSDictionary<PHCloudIdentifier *,PHLocalIdentifierMapping *> *) localIdentifierMappingsForSyncedCloudIdentifiers:(NSArray<PHCloudIdentifier *> *) cloudIdentifiers;
```

#### Discussion

This method can be very expensive so they should be used sparingly for batch lookup of all needed identifiers. Clients should work in terms of local identifiers and call these methods only once after loading from and before saving to persistent storage.  If the attempt to lookup a local identifier for a given cloud identifier fails, the error parameter will indicate the reason.

Use this method instead of `localIdentifierMappingsForCloudIdentifiers:` to avoid looking up PHAsset local identifiers based on the media content matching

## Parameters

- `cloudIdentifiers`: The array of `PHCloudIdentifier` instances whose local identifiers are being requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/localidentifiermappingsforsyncedcloudidentifiers:)*