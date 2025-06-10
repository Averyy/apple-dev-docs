# Preliminary_Behavior

**Framework**: RealityKit

A typed schema that combines one or more triggers with associated actions.

#### Overview

Because it inherits `Typed`, this schema declares a `Preliminary_Behavior` as a type of prim. For more information about typed schemas, see USD Specification > [`Typed`](https://developer.apple.comhttp://graphics.pixar.com/usd/docs/USD-Glossary.html#USDGlossary-TypedSchema).

To run actions based on a trigger, an asset defines a prim of this type and sets its [`triggers`](triggers.md) and [`actions`](actions.md).

##### Declaration

```other
class Preliminary_Behavior "Preliminary_Behavior" (
    inherits = </Typed>
)
```

##### Trigger Animation for a Tapped Cube

The following example demonstrates a behavior that applies an `EmphasizeAction` to a cube to flip it. Because the cube defines a tap trigger, the runtime performs the flip when a user taps the cube in an AR experience.

```other
#usda 1.0

def Preliminary_Behavior "TapAndFlip"
{
    rel triggers = [ <Tap> ]
    rel actions = [ <Entry> ]

    def Preliminary_Trigger "Tap" ( inherits = </TapGestureTrigger> )
    {
        rel affectedObjects = [ </Cube> ]
    }

    def Preliminary_Action "Entry" ( inherits = </GroupAction> )
    {
        uniform token type = "parallel"
        rel actions = [ <Flip> ]
    }

    def Preliminary_Action "Flip" ( inherits = </EmphasizeAction> )
    {
        rel affectedObjects = [ </Cube> ]
        uniform token motionType = "flip"
    }
}

def Cube "Cube" { }
```

## Topics

### Properties
- [triggers](triggers.md)
  A list of prims that execute a behavior’s actions.
- [actions](actions.md)
  A list of actions that make up the group.
- [exclusive](exclusive.md)
  A Boolean value that determines if a behavior executes exclusively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/preliminary-behavior)*