# reflection(functionName:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Retrieves reflection information for a function in the library.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func reflection(functionName: String) -> MTLFunctionReflection?
```

#### Return Value

An `MTLFunctionReflection` instance when the method succeeds; otherwise `nil`.

#### Discussion

The reflection instance contains metadata information about a specific GPU function, which can include:

- Function parameters
- Return types
- Bindings
- Annotations from a developer, if available

> **Note**: The Metal compiler generates the function’s reflection information when you or Xcode build the library.

The method only returns reflection information if all of the following conditions apply:

- The library has a function with a name that matches `functionName`.
- The deployment target is macOS 13.0 or later, or iOS 16.0 or later, or visionOS 2.0 or later.

## Parameters

- `functionName`: The name of a GPU function in the library.   The name needs to match one of the elements in the string array of library’s   property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllibrary/reflection(functionname:))*