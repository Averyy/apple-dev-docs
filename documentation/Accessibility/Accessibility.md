# Accessibility

**Framework**: Accessibility  
**Kind**: module

Make your apps accessible to everyone who uses Apple devices.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

#### Overview

Accessibility features help a wide range of people interact with their devices. By creating your app with accessibility in mind, you make it possible for everyone to enjoy your app. Whether you’re developing a new app, or updating an existing one, consider the needs of all the people who might use your app.

For many, accessibility is a necessity. For others, it’s a practicality. For example, closed captions can be necessary for someone who is deaf or hard of hearing, but also useful for someone watching a video in a noisy environment. Learn more about how to support different types of accessibility needs in your app using Apple’s wide range of accessibility APIs.

##### Dive Into Featured Sample Apps

Explore how sample apps leverage accessible design principles and accessibility APIs to create a great user experience for everyone.

##### Explore Assistive Technologies

People can personalize their devices by choosing the accessibility features and assistive technologies that give them the best user experience. Make sure your app provides a great experience for people who use assistive technologies by testing your app with them.

##### Add Accessibility Nutrition Labels to Your Product Page

You can add Accessibility Nutrition Labels to your App Store product page to indicate which accessibility features your app supports on each platform. For example, a person who is blind or has low vision might seek apps that support VoiceOver or Larger Text.

For more information on adding Accessibility Nutrition Labels to your app, see [`Overview of Accessibility Nutrition Labels`](https://developer.apple.comhttps://devcms.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels) in App Store Connect Help.

##### Related Videos

## Topics

### Essentials
- [Accessibility updates](../Updates/Accessibility.md)
  Learn about important changes to Accessibility.
- [Accessibility](https://developer.apple.com/design/Human-Interface-Guidelines/accessibility)
  Accessible user interfaces empower everyone to have a great experience with your app or game.
- [Performing accessibility testing for your app](performing-accessibility-testing-for-your-app.md)
  Test your app with accessibility settings and assistive technologies to discover and address accessibility issues.
### Sample code
- [Enhancing the accessibility of your SwiftUI app](enhancing-the-accessibility-of-your-swiftui-app.md)
  Support advancements in SwiftUI accessibility to make your app accessible to everyone.
- [Creating Accessible Views](../swiftui/creating_accessible_views.md)
  Make your app accessible to everyone by applying accessibility modifiers to your SwiftUI views.
- [Delivering an exceptional accessibility experience](delivering_an_exceptional_accessibility_experience.md)
  Make improvements to your app’s interaction model to support assistive technologies such as VoiceOver.
- [Integrating accessibility into your app](integrating_accessibility_into_your_app.md)
  Make your app more accessible to users with disabilities by adding accessibility features.
- [Accessibility design for Mac Catalyst](accessibility_design_for_mac_catalyst.md)
  Improve navigation in your app by using keyboard shortcuts and accessibility containers.
### Domains
- [Vision](vision.md)
  A person may be blind or color blind, or have a vision challenge that makes focusing difficult.
- [Speech](speech.md)
  A person may have a speech disability or prefer to connect without using their voice.
- [Mobility](mobility.md)
  A person with reduced mobility may have difficulty holding a device or tapping the interface.
- [Cognitive](cognitive.md)
  A person may have difficulty remembering a sequence of steps, or they may find an overly complex user interface difficult to process and manage.
- [Hearing](hearing.md)
  A person may be deaf, have partial hearing loss, or have difficulty hearing sounds within a certain range.
### Developer tools
- [Accessibility Inspector](accessibility-inspector.md)
  Reveal how your app represents itself to people using accessibility features.
### Assistive technologies
- [Assistive technologies](assistive-technologies.md)
  Make sure your app provides a great experience for people who use assistive technologies.
### Accessibility framework
- [Accessibility API](accessibility-api.md)
  Browse API in the Accessibility framework.
### Platforms
- [Accessibility fundamentals](../SwiftUI/Accessibility-fundamentals.md)
  Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Accessibility for UIKit](../UIKit/accessibility-for-uikit.md)
  Make your UIKit apps accessible to everyone who uses iOS and tvOS.
- [Accessibility for AppKit](../AppKit/accessibility-for-appkit.md)
  Make your AppKit apps accessible to everyone who uses macOS.
- [Accessibility for visionOS](accessibility-for-visionos.md)
  Make your apps accessible to everyone who uses visionOS.
### WWDC Challenges
- [WWDC22 Challenge: Learn Switch Control through gaming](wwdc22_challenge_learn_switch_control_through_gaming.md)
  Play a card-matching game using Switch Control.
- [WWDC21 Challenge: Large Text Challenge](wwdc21_challenge_large_text_challenge.md)
  Design for large text sizes by modifying the user interface.
- [WWDC21 Challenge: Speech Synthesizer Simulator](wwdc21_challenge_speech_synthesizer_simulator.md)
  Simulate a conversation using speech synthesis.
- [WWDC21 Challenge: VoiceOver Maze](wwdc21_challenge_voiceover_maze.md)
  Navigate to the end of a dark maze using VoiceOver as your guide.
### Classes
- [class AXBrailleTable](axbrailletable.md)
  A rule for translating print text to Braille, and back-translating Braille to print text.
- [class AXBrailleTranslationResult](axbrailletranslationresult.md)
  The result of translation or back-translation.
- [class AXBrailleTranslator](axbrailletranslator.md)
  Translates print text to Braille and Braille to print text according to the given Braille table.
- [class AXFeatureOverrideSession](axfeatureoverridesession.md)
  A token object that represents an override session held by your app.
- [class AXFeatureOverrideSessionManager](axfeatureoverridesessionmanager.md)
  A manager class to begin and end accessibility feature override sessions. Multiple override sessions are reconciled by combining the requests, preferring feature enablement. Ending all sessions restores the prior state of Accessibility feature enablement. Your app must be entitled with com.apple.developer.accessibility.merchant-api-control.
- [class AXMathExpression](axmathexpression.md)
- [class AXMathExpressionFenced](axmathexpressionfenced.md)
- [class AXMathExpressionFraction](axmathexpressionfraction.md)
- [class AXMathExpressionIdentifier](axmathexpressionidentifier.md)
- [class AXMathExpressionMultiscript](axmathexpressionmultiscript.md)
- [class AXMathExpressionNumber](axmathexpressionnumber.md)
- [class AXMathExpressionOperator](axmathexpressionoperator.md)
- [class AXMathExpressionRoot](axmathexpressionroot.md)
- [class AXMathExpressionRow](axmathexpressionrow.md)
- [class AXMathExpressionSubSuperscript](axmathexpressionsubsuperscript.md)
- [class AXMathExpressionTable](axmathexpressiontable.md)
- [class AXMathExpressionTableCell](axmathexpressiontablecell.md)
- [class AXMathExpressionTableRow](axmathexpressiontablerow.md)
- [class AXMathExpressionText](axmathexpressiontext.md)
- [class AXMathExpressionUnderOver](axmathexpressionunderover.md)
### Protocols
- [protocol AXMathExpressionProvider](axmathexpressionprovider.md)
### Structures
- [struct AXFeatureOverrideSessionError](axfeatureoverridesessionerror-swift.struct.md)
### Variables
- [let AXFeatureOverrideSessionErrorDomain: String](axfeatureoverridesessionerrordomain.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Accessibility)*