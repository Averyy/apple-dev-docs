---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argumenthelp"
framework: "swift-argument-parser/ArgumentParser"
---

# ArgumentHelp

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: struct  
**Role**: Structure

Help information for a command-line argument.

## Declaration

```swift
struct ArgumentHelp
```

## Mentions

- [Customizing Help](./customizinghelp.md)

## Topics

### Initializers
- [init(String, discussion: String?, valueName: String?, shouldDisplay: Bool)](./argumenthelp/init%28_,discussion,valuename,shoulddisplay%29.md)
  Creates a new help instance.
- [init(String, discussion: String?, valueName: String?, visibility: ArgumentVisibility, argumentType: (any ExpressibleByArgument.Type)?)](./argumenthelp/init%28_,discussion,valuename,visibility,argumenttype%29.md)
  Creates a new help instance.
### Instance Properties
- [var abstract: String](./argumenthelp/abstract.md)
  A short description of the argument.
- [var argumentType: (any ExpressibleByArgument.Type)?](./argumenthelp/argumenttype.md)
  A property of meta type `any ExpressibleByArgument.Type` that serves to retain information about any arguments that have enumerable values and their descriptions.
- [var discussion: String?](./argumenthelp/discussion.md)
  An expanded description of the argument, in plain text form.
- [var shouldDisplay: Bool](./argumenthelp/shoulddisplay.md)
  A Boolean value indicating whether this argument should be shown in the extended help display.
- [var valueName: String?](./argumenthelp/valuename.md)
  An alternative name to use for the argument’s value when showing usage information.
- [var visibility: ArgumentVisibility](./argumenthelp/visibility.md)
  A visibility level indicating whether this argument should be shown in the extended help display.
### Type Properties
- [static var hidden: ArgumentHelp](./argumenthelp/hidden.md)
  A `Help` instance that shows an argument only in the extended help display.
- [static var `private`: ArgumentHelp](./argumenthelp/private.md)
  A `Help` instance that hides an argument from the extended help display.
### Default Implementations
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](./argumenthelp/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringInterpolation Implementations](./argumenthelp/expressiblebystringinterpolation-implementations.md)
- [ExpressibleByStringLiteral Implementations](./argumenthelp/expressiblebystringliteral-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.Escapable
- Swift.ExpressibleByExtendedGraphemeClusterLiteral
- Swift.ExpressibleByStringInterpolation
- Swift.ExpressibleByStringLiteral
- Swift.ExpressibleByUnicodeScalarLiteral
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Property Customization
- [Customizing Help](./customizinghelp.md)
  Support your users (and yourself) by providing rich help for arguments, options, and flags.
- [struct ArgumentVisibility](./argumentvisibility.md)
  Visibility level of an argument’s help.
- [struct NameSpecification](./namespecification.md)
  A specification for how to represent a property as a command-line argument label.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argumenthelp)*