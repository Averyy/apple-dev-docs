# init(page:usage:)

**Framework**: Core HID  
**Kind**: init  
**Role**: Initializer

Creates a HID usage page from raw page and usage values.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init(page: UInt16, usage: UInt16?)
```

## Discussion

Unsupported cases are returned as [`HIDUsage.generic(_:_:)`](./generic%28_,_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidusage/init(page:usage:))*