# UISceneInitialImmersionStyle

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

Provide a preferred initial scene style for an immersive space scene.

**Availability**:
- visionOS 1.0+

## Details

- **Name**: `UISceneInitialImmersionStyle`
- **Type**: string

## Possible Values

- `UIImmersionStyleFull`
- `UIImmersionStyleMixed`
- `UIImmersionStyleProgressive`

## Discussion

Use [`UISceneInitialImmersionStyle`](./uisceneinitialimmersionstyle.md) to configure the initial style for the system to use to create an immersive space scene for your app.

> **Note**:  The system uses an appropriate alternate when the environment can’t support the preferred style you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiscenesessionroleimmersivespaceapplication/uisceneinitialimmersionstyle)*