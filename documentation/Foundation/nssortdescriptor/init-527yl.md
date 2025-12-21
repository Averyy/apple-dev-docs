# init(_:)

**Framework**: Foundation  
**Kind**: init

Creates an `NSSortDescriptor` representing the same sort as the given `SortDescriptor`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: iOS 17, macOS 14, tvOS 17, watchOS 10)
convenience init<Compared>(_ sortDescriptor: SortDescriptor<Compared>) where Compared : NSObject
```

## Parameters

- `sortDescriptor`: The   to convert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssortdescriptor/init(_:)-527yl)*