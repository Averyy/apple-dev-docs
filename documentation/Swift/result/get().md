# get()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns the success value as a throwing expression.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
consuming func get() throws(Failure) -> Success
```

Available when `Failure` conforms to `Error`.

## Return Value

The success value, if the instance represents a success.

## Discussion

Use this method to retrieve the value of this result if it represents a success, or to catch the value if it represents a failure.

```swift
let integerResult: Result<Int, Error> = .success(5)
do {
    let value = try integerResult.get()
    print("The value is \(value).")
} catch {
    print("Error retrieving the value: \(error)")
}
// Prints "The value is 5."
```

> **Throws**: The failure value, if the instance represents a failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/get())*