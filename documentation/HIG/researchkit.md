---
url: https://developer.apple.com/design/human-interface-guidelines/researchkit
framework: HIG
---

# ResearchKit

**Type:** article

**Platforms:** ios, ipados

> **Updated 2023-09-12:** Updated artwork.

A research app lets people everywhere participate in important medical research studies.

![A sketch of the ResearchKit icon. The image is overlaid with rectangular and circular grid lines and is tinted blue to subtly reflect the blue in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/52b18da535d1796e5fa006ff40e0fbae/technologies-ResearchKit-intro~dark%402x.png)
The ResearchKit framework provides predesigned screens and transitions that make it easy to design and build an engaging custom research app. For developer guidance, see [Research & Care > ResearchKit](https://www.researchandcare.org/researchkit/).

## Creating the onboarding experience
When opening a research app for the first time, people encounter a series of screens that introduce them to the study, determine their eligibility to participate, request permission to proceed with the study, and, when appropriate, grant access to personal data. These screens aren’t typically revisited once they’ve been completed, so clarity is essential.
**Always display the onboarding screens in the correct order.**
![A diagram showing four boxes in a horizontal row. Beginning with the leftmost box, an arrow pointing toward the right connects each box to the next. From the left, the boxes are labeled Introduction, Eligibility, Informed consent, and Permission to access data.](https://docs-assets.developer.apple.com/published/bc85befc3e83427772332aec1a3df10b/researchkit-diagram~dark%402x.png)

### 1. Introduction
**Provide an introduction that informs and provides a call to action.** Clearly describe the subject and purpose of your study. Also allow existing participants to quickly log in and continue an in-progress study.
![A screenshot that shows a ResearchKit app's introductory screen on iPhone, which invites someone to join a study.](https://docs-assets.developer.apple.com/published/b2e12c8eeedeb58c2b31f6da926be952/introduction-screen%402x.png)

### 2. Determine eligibility
**Determine eligibility as soon as possible.** People don’t need to move on to the consent section if they’re not eligible for the study. Only present eligibility requirements that are necessary for your study. Use simple, straightforward language that describes the requirements, and make it easy to enter information.
![A screenshot that shows a ResearchKit app's eligibility screen on iPhone. The screen includes fields that ask for a person's age, location, and type of smartphone. The bottom of the screen includes 'Back' and 'Submit' buttons, and the top of the screen includes a button for returning to the previous screen and a button for help.](https://docs-assets.developer.apple.com/published/c458c3b78dc70a5ec20e2fbcfdfcce32/eligibility-screen%402x.png)

### 3. Get informed consent
**Make sure participants understand your study before you get their consent.** ResearchKit helps you make the consent process concise and friendly, while still allowing you to incorporate into the consent any legal requirements or requirements set by an institutional review board or ethics review board. Make sure that your app complies with the applicable App Store Guidelines, including the consent requirements. Typically, the consent section explains how the study works, ensures that participants understand the study and their responsibilities, and gets the participant’s consent.
**Break a long consent form into easily digestible sections.** Each section can cover one aspect of the study, such as data gathering, data use, potential benefits, possible risks, time commitment, how to withdraw, and so on. For each section, use simple, straightforward language to provide a high-level overview. If necessary, provide a more detailed explanation of the section that participants can read by tapping a Learn More button. Participants need to be able to view the entire consent form before they agree to participate.
**If it makes sense, provide a quiz that tests the participant’s understanding.** You might do this for questions the participant would otherwise be asked when obtaining consent in person.
![A screenshot that shows a ResearchKit app's quiz screen on iPhone. The screen displays a multiple-choice question designed to make sure people understand the study. The bottom of the screen includes a 'Next' button, and the top of the screen includes a button for returning to the previous screen and a button for help.](https://docs-assets.developer.apple.com/published/09184ffb5a698e998d39bb44458911a8/consent-quiz-screen%402x.png)
**Get the participant’s consent and, if appropriate, some contact information.** After agreeing to join the study, participants receive a confirmation dialog, followed by screens in which they provide their signature and contact details. Most research apps email participants a PDF version of the consent form for their records.
![A screenshot that shows a ResearchKit app's consent screen on iPhone. The screen recaps key points about the study, shows the person's name, and asks the person to confirm whether they'd like to participate in the study. The bottom of the screen includes 'Disagree' and 'Accept' buttons, and the top of the screen includes a button for returning to the previous screen and a button for help.](https://docs-assets.developer.apple.com/published/46b3fb7e5f95abccac05269223545a05/consent-signature-screen%402x.png)

### 4. Request permission to access data
**Get permission to access the participant’s device or data, and to send notifications.** Clearly explain why your research app needs access to location, Health, or other data, and don’t request access to data that isn’t critical to your study. If your app requires it, also ask for permission to send notifications to the participant’s device.
![A screenshot that shows a ResearchKit app's consent screen on iPhone. The screen recaps key points about the study, and offers the choice to share data with researchers for future research purposes, or only for this particular study. The bottom of the screen includes an 'Accept' button, and the top of the screen includes a button for returning to the previous screen and a button for help.](https://docs-assets.developer.apple.com/published/bcceaf89b0a6997c37f5179229674b84/permissions-health-data-screen%402x.png)

## Conducting research
To get input from participants, your study might use surveys, active tasks, or a combination of both. Depending on the architecture of your study, participants may interact with each section multiple times or only once.
**Create surveys that keep participants engaged.** ResearchKit provides many customizable screens you can use in your surveys, and makes it easy to present questions that require different types of answers, such as true or false, multiple choice, dates and times, sliding scales, and open-ended text entry. As you use ResearchKit screens to design a survey, follow these guidelines to provide a great experience:
- Tell participants how many questions there are and about how long the survey will take.
- Use one screen per question.
- Show participants their progress in the survey.
- Keep the survey as short as possible. Several short surveys tend to work better than one long survey.
- For questions that require some additional explanation, use the standard font for the question and a slightly smaller font for the explanatory text.
- Tell participants when the survey is complete.
![A screenshot that shows a ResearchKit app's survey screen on iPhone. This particular screen asks someone to specify Parkinson's disease symptoms from a list and tap a 'Next' button to continue the survey. The top of the screen includes a 'Close' button.](https://docs-assets.developer.apple.com/published/ee125d1de4ec07f41856c9bab67ee0c3/survey-question-type1-screen%402x.png)
**Make active tasks easy to understand.** An active task requires the participant to engage in an activity, such as speaking into the microphone, tapping fingers on the screen, walking, or performing a memory test. Follow these guidelines to encourage participants to perform an active task and give them the best chance of success:
- Describe how to perform the task using clear, simple language.
- Explain any requirements, such as if the task must be performed at a particular time or under specific circumstances.
- Make sure participants can tell when the task is complete.
![A screenshot that shows a ResearchKit app's active task screen on iPhone. This particular screen shows an illustration of a person walking, and instructions that explain how to perform a Walk and Balance active task. A list of requirements is shown, along with a 'Get started' button. The top of the screen includes a 'Close' button.](https://docs-assets.developer.apple.com/published/efdeed00e3196a8eaea5155ff78b0015/active-tasks-screen%402x.png)

## Managing personal information and providing encouragement
ResearchKit offers a profile screen you can use to let participants manage personal information while they’re in your research app. It’s also a good idea to design a custom screen that motivates people and gives them a way to track progress in the study. Ideally, both screens are accessible at all times in your app.
**Use a profile to help participants manage personal data related to your study.** A profile screen can let people edit data that might change during the course of the study — such as weight or sleep habits — and remind them of upcoming activities. A profile screen can also provide an easy way to leave a study and view important information, such as the consent document and privacy policy.
![A screenshot that shows a ResearchKit app's profile screen on iPhone. This particular screen includes a list of fields for personal information like name and birth year. Each field includes a button for editing the field's value. The top of the screen includes a settings button, and the bottom of the screen includes tabs for 'Tracking', 'History' and 'Profile'. The active tab is 'Profile'.](https://docs-assets.developer.apple.com/published/9112be9b40dfaec1cc5270f94adc4645/profile-screen%402x.png)
**Use a dashboard to show progress and motivate participants to continue.** If appropriate for your study, use a dashboard to provide encouraging feedback, such as daily progress, weekly assessments, results from specific activities, and even results that compare the participant’s results with aggregated results from others in the study.
![A screenshot that shows a ResearchKit app's history screen on iPhone. This particular screen shows a log of active tasks performed over two days. The bottom of the screen includes tabs for 'Tracking', 'History' and 'Profile'. The active tab is 'History'.](https://docs-assets.developer.apple.com/published/d5c1639ec410f2064db916c146e27f17/dashboard-screen%402x.png)

## Platform considerations
*No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.*

## Resources

#### Related
[Research & Care > ResearchKit](https://www.researchandcare.org/researchkit/)

#### Developer documentation
[Research & Care > Developers](https://www.researchandcare.org/developers/)
[Protecting user privacy](../HealthKit/protecting-user-privacy.md) — HealthKit
[ResearchKit GitHub project](https://github.com/ResearchKit/ResearchKit)

#### Videos
- [What's new in CareKit](https://developer.apple.com/videos/play/wwdc2020/10151) - Build feature-rich research and care apps with CareKit: Learn about the latest advancements to our health framework, including new views for its modular architecture, improvements to the data store, and tighter integration with other frameworks on iOS. And discover how the open-source community continues to leverage CareKit to allow developers to push the boundaries of digital health&nbsp;—&nbsp;all while preserving privacy.
- [Build a research and care app, part 1: Setup onboarding](https://developer.apple.com/videos/play/wwdc2021/10068) - Learn how ResearchKit and CareKit can work together to take the tedium out of paper surveys. Code along with us and build a working care pilot app. Explore best practices for onboarding and consent with ResearchKit, and find out how your app can require participants to sign consent documents by leveraging CareKit’s store and UI components.

This is the first session in a three-part Code-Along series. To get the most out of this series, we recommend that you have some basic familiarity with both ResearchKit and CareKit. For more background, watch "ResearchKit and CareKit Reimagined” from WWDC19.
- [ResearchKit and CareKit Reimagined](https://developer.apple.com/videos/play/wwdc2019/217) - The ResearchKit and CareKit frameworks are the fastest route to delivering powerful native iOS apps for the research and patient care field.  Learn about the newest audio and speech active-tasks, a completely redesigned user experience, and modular architecture designed to make it a breeze to create care plan apps for any use case.

## Change log
| Date | Changes |
| --- | --- |
| September 12, 2023 | Updated artwork. |




---
*Source: [https://developer.apple.com/design/human-interface-guidelines/researchkit](https://developer.apple.com/design/human-interface-guidelines/researchkit)*
