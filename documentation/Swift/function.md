# function()

**Framework**: Swift  
**Kind**: macro

Produces the name of the declaration in which it appears.

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
@freestanding
(expression) macro function<T>() -> T where T : ExpressibleByStringLiteral
```

#### Overview

Inside a function, the value `#function` produces is the name of that function, inside a method it’s the name of that method, inside a property getter or setter it’s the name of that property, inside special members like `init` or `subscript` it’s the name of that keyword, and at the top level of a file it’s the name of the current module.

When used as the default value of a function or method parameter, this macro’s value is determined when the default value expression is evaluated at the call site. For example:

```swift
func logFunctionName(string: String = #function) {
    print(string)
}
func myFunction() {
    logFunctionName() // Prints "myFunction()".
}
```

## See Also

- [macro file<T>() -> T](file().md)
  Produces the path to the file in which it appears.
- [macro fileID<T>() -> T](fileid().md)
  Produces a unique identifier for the source file in which the macro appears.
- [macro filePath<T>() -> T](filepath().md)
  Produces the complete path to the file in which the macro appears.
- [macro line<T>() -> T](line().md)
  Produces the line number on which it appears.
- [macro column<T>() -> T](column().md)
  Produces the column number in which the macro begins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/function())*