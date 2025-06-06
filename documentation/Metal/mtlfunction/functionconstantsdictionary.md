# functionConstantsDictionary

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A dictionary of function constants for a specialized function.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var functionConstantsDictionary: [String : MTLFunctionConstant] { get }
```

#### Discussion

This property returns a dictionary of the function constants that you need to provide to specialize this function. This property returns an empty dictionary if this function is already specialized or doesn’t declare any function constants.

To create the specialized function, set these constant values in a new [`MTLFunctionConstantValues`](mtlfunctionconstantvalues.md) object and call the [`makeFunction(name:constantValues:completionHandler:)`](mtllibrary/makefunction(name:constantvalues:completionhandler:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunction/functionconstantsdictionary)*