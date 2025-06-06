# interactive

**Framework**: File Provider  
**Kind**: property

A testing mode where the extension can deterministically test asynchronous operations.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
static var interactive: NSFileProviderDomain.TestingModes { get }
```

#### Discussion

Disable the system’s automatic scheduling and execution of operations. Instead, the File Provider extension can manually determine the order of execution.

This testing mode enables the following synchronous methods:

The [`interactive`](nsfileproviderdomain/testingmodes-swift.struct/interactive.md) testing mode expects the File Provider extension to repeat the following steps while running tests:

1. Call [`listAvailableTestingOperations()`](nsfileprovidermanager/listavailabletestingoperations().md)to get the list of outstanding operations.
2. Select the next set of operations required by your test.
3. Call [`run(_:)`](nsfileprovidermanager/run(_:).md)to execute those operations.

The `interactive` testing mode also disables some of the File Provider extension’s crash guarantees. For example, the system may lose any event that it hasn’t yet ingested.

## See Also

- [static var alwaysEnabled: NSFileProviderDomain.TestingModes](nsfileproviderdomain/testingmodes-swift.struct/alwaysenabled.md)
  A testing mode that automatically enables the domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain/testingmodes-swift.struct/interactive)*