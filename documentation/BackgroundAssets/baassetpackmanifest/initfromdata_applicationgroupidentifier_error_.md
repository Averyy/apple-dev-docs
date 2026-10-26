# initFromData:applicationGroupIdentifier:error:

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Initializes a representation of a manifest in memory from JSON-encoded data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (instancetype) initFromData:(NSData *) data applicationGroupIdentifier:(NSString *) applicationGroupIdentifier error:(NSError **) error;
```

## Parameters

- `data`: JSON-encoded data.
- `applicationGroupIdentifier`: The identifier of the application group in which to store unmanaged asset packs that are downloaded from the manifest.
- `error`: A pointer to an error that will be set if an error occurs.

## See Also

### Creating an asset pack manifest
- [- initWithContentsOfURL:applicationGroupIdentifier:error:](./initwithcontentsofurl_applicationgroupidentifier_error_.md)
  Initializes a representation of a manifest in memory given a URL to the manifest’s representation as a JSON file on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanifest/initfromdata:applicationgroupidentifier:error:)*