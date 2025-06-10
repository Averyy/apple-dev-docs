# run(_:)

**Framework**: File Provider  
**Kind**: method

Asks the system to schedule and execute the specified operations.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
func run(_ operations: [any NSFileProviderTestingOperation]) throws -> [AnyHashable : any Error]
```

#### Discussion

> ❗ **Important**:  Before calling this method, you must set the domain’s [`testingModes`](nsfileproviderdomain/testingmodes-swift.property.md) property to include the [`interactive`](nsfileproviderdomain/testingmodes-swift.struct/interactive.md) value.

The system waits until all of the specified operations complete and reports an error for any operations that fail.

## Parameters

- `operations`: An array of operations. Populate this array with one or more operations returned by the   method.

## See Also

- [func listAvailableTestingOperations() throws -> [any NSFileProviderTestingOperation]](nsfileprovidermanager/listavailabletestingoperations.md)
  Lists all the operations that are ready for scheduling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/run(_:))*