# withObservationTracking(_:onChange:)

**Framework**: Observation  
**Kind**: func

Tracks access to properties.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func withObservationTracking<T>(_ apply: () -> T, onChange: @autoclosure () -> () -> Void) -> T
```

#### Return Value

The value that the `apply` closure returns if it has a return value; otherwise, there is no return value.

#### Discussion

This method tracks access to any property within the `apply` closure, and informs the caller of value changes made to participating properties by way of the `onChange` closure. For example, the following code tracks changes to the name of cars, but it doesn’t track changes to any other property of `Car`:

```swift
func render() {
    withObservationTracking {
        for car in cars {
            print(car.name)
        }
    } onChange: {
        print("Schedule renderer.")
    }
}
```

## Parameters

- `apply`: A closure that contains properties to track.
- `onChange`: The closure invoked when the value of a property changes.

## See Also

- [struct ObservationRegistrar](observationregistrar.md)
  Provides storage for tracking and access to data changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/observation/withobservationtracking(_:onchange:))*