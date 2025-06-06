# allOf(requirement:)

**Framework**: LightweightCodeRequirements  
**Kind**: method

Create a [`ProcessCodeRequirement`](processcoderequirement.md) that requires matching all of the provided constraints.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
static func allOf(@ProcessConstraintBuilder requirement: () -> [any ProcessConstraint]) throws -> ProcessCodeRequirement
```

#### Discussion

This operation will throw ConstraintError.duplicateKeys if more than one constraint of the same type is found in the same logical grouping. For example the following snippets will throw:

```swift
    let req1 = try ProcessCodeRequirement.allOf {
        SigningIdentifier("com.apple.ls")
        SigningIdentifier("com.apple.ps")
    }
    let req2 = try ProcessCodeRequirement.allOf {
           SigningIdentifier("com.apple.ls")
           anyOf {
               SigningIdentifier("com.apple.ps")
           }
    }
    let req3 = try ProcessCodeRequirement.allOf {
        SigningIdentifier("com.apple.ls")
        allOf {
            ValidationCategory(.platform)
            SigningIdentifier("com.apple.ps")
        }
    }
```

The second requirement throws because a single constraint within anyOf provides no option and so it gets lifted to the higher logical group. Similarly, the third requirement throws because an allOf operation nested in an allOf operation has no logical effect, so all of the constraints in the nested operation get lifted into the higher level group. On the other hand the following snippet will not throw:

```swift
    let req4 = try ProcessCodeRequirement.allOf {
        anyOf {
            SigningIdentifier("com.apple.ls")
            ValidationCategory(.platform)
        }
        anyOf {
            SigningIdentifier("com.apple.ps")
            ValidationCategory(.platform)
        }
    }
```

In this requirement, both anyOf operations provide a choice, so the two groups are considered separate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/processcoderequirement/allof(requirement:))*