# setBusCount(_:)

**Framework**: Audiotoolbox  
**Kind**: method

Changes the number of busses in the array.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setBusCount(_ count: Int) throws
```

#### Discussion

- [`false`](https://developer.apple.com/documentation/swift/false) if the operation failed.

#### Discussion

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `count`: The new number of busses in the array.

## See Also

- [var count: Int](auaudiounitbusarray/count.md)
  The number of busses in the array.
- [var isCountChangeable: Bool](auaudiounitbusarray/iscountchangeable.md)
  Determines whether the array can have a variable number of busses.
- [var ownerAudioUnit: AUAudioUnit](auaudiounitbusarray/owneraudiounit.md)
  The audio unit that owns the bus array.
- [var busType: AUAudioUnitBusType](auaudiounitbusarray/bustype.md)
  Determines whether the bus array is for input or output.
- [subscript(Int) -> AUAudioUnitBus](auaudiounitbusarray/subscript(_:).md)
  Returns the bus at the specified index.
- [func addObserver(toAllBusses: NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](auaudiounitbusarray/addobserver(toallbusses:forkeypath:options:context:).md)
  Adds a KVO observer for a given property on all busses in the array.
- [func removeObserver(fromAllBusses: NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](auaudiounitbusarray/removeobserver(fromallbusses:forkeypath:context:).md)
  Removes a KVO observer for a given property on all busses in the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/setbuscount(_:))*