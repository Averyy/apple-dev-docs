# init(insertionIndexPath:reuseIdentifier:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a placeholder object with the specified index path and reuse identifier.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(insertionIndexPath: IndexPath, reuseIdentifier: String)
```

```objc
- (instancetype) initWithInsertionIndexPath:(NSIndexPath *) insertionIndexPath reuseIdentifier:(NSString *) reuseIdentifier;
```

#### Return Value

A new placeholder cell object.

## Parameters

- `insertionIndexPath`: The index path at which to insert the placeholder cell.
- `reuseIdentifier`: The reuse identifier to use when dequeueing the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewplaceholder/init(insertionindexpath:reuseidentifier:))*