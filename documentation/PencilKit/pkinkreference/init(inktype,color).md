# init(inkType:color:)

**Framework**: PencilKit  
**Kind**: init  
**Role**: Initializer

Create a new ink, specifying its type, color.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
init(inkType type: __PKInkType, color: UIColor)
```

*macOS*

```swift
init(inkType type: __PKInkType, color: NSColor)
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
- (instancetype) initWithInkType:(PKInkType) type color:(UIColor *) color;
```

*macOS*

```objc
- (instancetype) initWithInkType:(PKInkType) type color:(NSColor *) color;
```

## Parameters

- `type`: The type of ink to create, from one of the available [`PKInkType`](../pkinktype.md) enumerations.
- `color`: The base color for this ink.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkreference/init(inktype:color:))*