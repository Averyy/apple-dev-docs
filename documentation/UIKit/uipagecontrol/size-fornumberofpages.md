# size(forNumberOfPages:)

**Framework**: UIKit  
**Kind**: method

Returns the size the receiver’s bounds should be to accommodate the given number of pages.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func size(forNumberOfPages pageCount: Int) -> CGSize
```

#### Return Value

The minimum size required to display dots for the page count.

#### Discussion

Subclasses that customize the appearance of the page control can use this method to resize the page control when the page count changes.

## Parameters

- `pageCount`: The number of pages to fit in the receiver’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/size(fornumberofpages:))*