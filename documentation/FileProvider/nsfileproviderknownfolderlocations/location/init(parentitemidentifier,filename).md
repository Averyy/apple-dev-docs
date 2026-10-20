# init(parentItemIdentifier:filename:)

**Framework**: File Provider  
**Kind**: init  
**Role**: Initializer

Initialize a location with the filename of the folder in a specified parent.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init(parentItemIdentifier: NSFileProviderItemIdentifier, filename: String)
```

```objc
- (instancetype) initWithParentItemIdentifier:(NSFileProviderItemIdentifier) parentItemIdentifier filename:(NSString *) filename;
```

#### Discussion

When replicating a known folder the system will reuse a folder located at the specified filename within the parent if one exists, or create a new item at this location if none exists yet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderknownfolderlocations/location/init(parentitemidentifier:filename:))*