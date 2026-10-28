# extensionWillDiscardDataSource()

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method

Provides an opportunity to use the data source before it’s released.

**Availability**:
- macOS 10.14+

## Declaration

```swift
optional func extensionWillDiscardDataSource()
```

```objc
- (void) extensionWillDiscardDataSource;
```

## Discussion

After this call, the extension context no longer strongly references the data source. Fetch any last data you need here before the data source goes out of scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojecttypedescriptiondatasource/extensionwilldiscarddatasource())*