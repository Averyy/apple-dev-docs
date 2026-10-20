# Accessibility

**Framework**: Accessibility  
**Kind**: module  
**Role**: Framework

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

- [Vision](./vision.md)
  A person may be blind or color blind, or have a vision challenge that makes focusing difficult.
- [Speech](./speech.md)
  A person may have a speech disability or prefer to connect without using their voice.
- [Mobility](./mobility.md)
  A person with reduced mobility may have difficulty holding a device or tapping the interface.
- [Cognitive](./cognitive.md)
  A person may have difficulty remembering a sequence of steps, or they may find an overly complex user interface difficult to process and manage.
- [Hearing](./hearing.md)
  A person may be deaf, have partial hearing loss, or have difficulty hearing sounds within a certain range.

##### Dive into featured sample apps

Explore how sample apps leverage accessible design principles and accessibility APIs to create a great user experience for everyone.

- [Destination Video](../visionOS/destination-video.md)
  Leverage SwiftUI to build an immersive media experience in a multiplatform app.
- [Happy Beam](../visionOS/happybeam.md)
  Leverage a Full Space to create a fun game using ARKit.

##### Explore assistive technologies

People can personalize their devices by choosing the accessibility features and assistive technologies that give them the best user experience. Make sure your app provides a great experience for people who use assistive technologies by testing your app with them.

- [VoiceOver](./voiceover.md)
  A gesture-based screen reader that provides an auditory description of the content onscreen.
- [Voice Control](./voice-control.md)
  An interface for navigating a device using voice commands to tap, swipe, type, and more.
- [Switch Control](./switch-control.md)
  An interface for navigating a device with a variety of adaptive switch hardware, wireless game controllers, or sounds such as a click or a pop.
- [Assistive Access](./assistive-access.md)
  A mode that tailors the iOS and iPadOS experience for people with cognitive disabilities.

##### Add Accessibility Nutrition Labels to your product page

You can add Accessibility Nutrition Labels to your App Store product page to indicate which accessibility features your app supports on each platform. For example, a person who is blind or has low vision might seek apps that support VoiceOver or Larger Text.

For more information on adding Accessibility Nutrition Labels to your app, see [Overview of Accessibility Nutrition Labels](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels) in App Store Connect Help.

##### Related videos

- [Create accessible spatial experiences](https://developer.apple.com/videos/play/wwdc2023/10034)
  Learn how you can make spatial computing apps that work well for everyone. Like all Apple platforms, visionOS is designed for accessibility: We’ll share how we’ve reimagined assistive technologies like VoiceOver and Pointer Control and designed features like Dwell Control to help people interact in the way that works best for them. Learn best practices for vision, motor, cognitive, and hearing accessibility and help everyone enjoy immersive experiences for visionOS.
- [Build accessible apps with SwiftUI and UIKit](https://developer.apple.com/videos/play/wwdc2023/10036)
  Discover how advancements in UI frameworks make it easier to build rich, accessible experiences. Find out how technologies like VoiceOver can better interact with your app’s interface through accessibility traits and actions. We’ll share the latest updates to SwiftUI that help you refine your accessibility experience and show you how to keep accessibility information up-to-date in your UIKit apps.
- [Meet Assistive Access](https://developer.apple.com/videos/play/wwdc2023/10032)
  Learn how Assistive Access can help people with cognitive disabilities more easily use iPhone and iPad. Discover the design principles that guide Assistive Access and find out how the system experience adapts to lighten cognitive load. We’ll show you how Assistive Access works and what you can do to support this experience in your app.
- [Design considerations for vision and motion](https://developer.apple.com/videos/play/wwdc2023/10078)
  Learn how to design engaging immersive experiences for visionOS that respect the limitations of human vision and motion perception. We’ll show you how you can use depth cues, contrast, focus, and motion to keep people comfortable as they enjoy your apps and games.
- [Perform accessibility audits for your app](https://developer.apple.com/videos/play/wwdc2023/10035)
  Discover how you can test your app for accessibility with every build. Learn how to perform automated audits for accessibility using XCTest and find out how to interpret the results. We’ll also share enhancements to the accessibility API that can help you improve UI test coverage.
- [Extend Speech Synthesis with personal and custom voices](https://developer.apple.com/videos/play/wwdc2023/10033)
  Bring the latest advancements in Speech Synthesis to your apps. Learn how you can integrate your custom speech synthesizer and voices into iOS and macOS. We’ll show you how SSML is used to generate expressive speech synthesis, and explore how Personal Voice can enable your augmentative and assistive communication app to speak on a person’s behalf in an authentic way.

## Topics

### Essentials
- [Accessibility updates](../Updates/accessibility.md)
  Learn about important changes to Accessibility.
- [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
  Accessible user interfaces empower everyone to have a great experience with your app or game.
- [Performing accessibility testing for your app](./performing-accessibility-testing-for-your-app.md)
  Test your app with accessibility settings and assistive technologies to discover and address accessibility issues.
### Sample code
- [Enhancing the accessibility of your SwiftUI app](./enhancing-the-accessibility-of-your-swiftui-app.md)
  Support advancements in SwiftUI accessibility to make your app accessible to everyone.
- [Creating accessible views](../SwiftUI/creating-accessible-views.md)
  Make your app accessible to everyone by applying accessibility modifiers to your SwiftUI views.
- [Delivering an exceptional accessibility experience](./delivering_an_exceptional_accessibility_experience.md)
  Make improvements to your app’s interaction model to support assistive technologies such as VoiceOver.
- [Integrating accessibility into your app](./integrating-accessibility-into-your-app.md)
  Make your app more accessible to users with disabilities by adding accessibility features.
- [Accessibility design for Mac Catalyst](./accessibility_design_for_mac_catalyst.md)
  Improve navigation in your app by using keyboard shortcuts and accessibility containers.
### Domains
- [Vision](./vision.md)
  A person may be blind or color blind, or have a vision challenge that makes focusing difficult.
- [Speech](./speech.md)
  A person may have a speech disability or prefer to connect without using their voice.
- [Mobility](./mobility.md)
  A person with reduced mobility may have difficulty holding a device or tapping the interface.
- [Cognitive](./cognitive.md)
  A person may have difficulty remembering a sequence of steps, or they may find an overly complex user interface difficult to process and manage.
- [Hearing](./hearing.md)
  A person may be deaf, have partial hearing loss, or have difficulty hearing sounds within a certain range.
### Developer tools
- [Accessibility Inspector](./accessibility-inspector.md)
  Reveal how your app represents itself to people using accessibility features.
### Assistive technologies
- [Assistive technologies](./assistive-technologies.md)
  Make sure your app provides a great experience for people who use assistive technologies.
### Accessibility framework
- [Accessibility API](./accessibility-api.md)
  Browse API in the Accessibility framework.
### Platforms
- [Accessibility fundamentals](../SwiftUI/accessibility-fundamentals.md)
  Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Accessibility for UIKit](../UIKit/accessibility-for-uikit.md)
  Make your UIKit apps accessible to everyone who uses iOS and tvOS.
- [Accessibility for AppKit](../AppKit/accessibility-for-appkit.md)
  Make your AppKit apps accessible to everyone who uses macOS.
- [Accessibility for visionOS](./accessibility-for-visionos.md)
  Make your apps accessible to everyone who uses visionOS.
### WWDC Challenges
- [WWDC22 Challenge: Learn Switch Control through gaming](./wwdc22_challenge_learn_switch_control_through_gaming.md)
  Play a card-matching game using Switch Control.
- [WWDC21 Challenge: Large Text Challenge](./wwdc21_challenge_large_text_challenge.md)
  Design for large text sizes by modifying the user interface.
- [WWDC21 Challenge: Speech Synthesizer Simulator](./wwdc21_challenge_speech_synthesizer_simulator.md)
  Simulate a conversation using speech synthesis.
- [WWDC21 Challenge: VoiceOver Maze](./wwdc21_challenge_voiceover_maze.md)
  Navigate to the end of a dark maze using VoiceOver as your guide.
### Resources
- [Specifications](./specifications.md)
  A collection of specification and reference documents related to accessibility technologies on Apple platforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Accessibility)*