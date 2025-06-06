# anyOf(requirement:)

**Framework**: LightweightCodeRequirements  
**Kind**: method

Create a [`LaunchCodeRequirement`](launchcoderequirement.md) that requires matching any of the provided constraints.

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
static func anyOf(@LaunchConstraintBuilder requirement: () -> [any LaunchConstraint]) throws -> LaunchCodeRequirement
```

#### Discussion

This operation will throw ConstraintError.duplicateKeys if more than one constraint of the same type is found in the same logical grouping. For example the following snippets will throw:

```swift
    let req1 = try LaunchCodeRequirement.anyOf {
        SigningIdentifier("com.apple.ls")
        SigningIdentifier("com.apple.ps")
    }
    let req2 = try LaunchCodeRequirement.anyOf {
           SigningIdentifier("com.apple.ls")
           allOf {
               SigningIdentifier("com.apple.ps")
           }
    }
    let req3 = try LaunchCodeRequirement.anyOf {
        SigningIdentifier("com.apple.ls")
        anyOf {
            ValidationCategory(.platform)
            SigningIdentifier("com.apple.ps")
        }
    }
```

The second requirement throws because a single constraint within allOf has no effect and so it gets lifted to the higher logical group. Similarly, the third requirement throws because an anyOf operation nested in an anyOf operation has no logical effect, so all of the constraints in the nested operation get lifted into the higher level group. On the other hand the following snippet will not throw:

```swift
    let req4 = try LaunchCodeRequirement.anyOf {
        allOf {
            SigningIdentifier("com.apple.ls")
            ValidationCategory(.platform)
        }
        allOf {
            SigningIdentifier("com.apple.ps")
            ValidationCategory(.platform)
        }
    }
```

In this requirement, both allOf operations provide different requirements that are each options., so the two groups are considered separate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/launchcoderequirement/anyof(requirement:))*